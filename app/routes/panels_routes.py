from datetime import datetime
from flask import Blueprint, request, jsonify, abort
from ..models.panels import db, Panels
from ..models.caregivers import Caregivers
from flask_jwt_extended import jwt_required, get_jwt_identity

panels_bp = Blueprint("panels", __name__, url_prefix="/api/panels")

@panels_bp.route("/<string:device_id>/config", methods=["GET"])
def get_config(device_id):
    """Lo consulta el ESP32 cada 30 s."""
    panel = Panels.query.get(device_id)
    if not panel or not panel.patient_id:
        return jsonify({"assigned": False}), 200

    # heartbeat
    panel.last_seen = datetime.utcnow()
    from .. import db
    db.session.commit()

    # extraigo la lista de IDs de cuidador
    caregiver_ids = [c.caregiver_id for c in panel.caregivers]

    return jsonify({
        "assigned":      True,
        "patient_id":    panel.patient_id,
        "caregiver_ids": caregiver_ids
    }), 200

@panels_bp.route('/checkAssignment/<string:device_id>', methods=['GET'])
@jwt_required(locations=['cookies'])
def check_panel_assigned(device_id):
    """
    1) Verifica si existe un panel con este device_id y está vinculado a un paciente.
    2) Si es así, añade al cuidador que hace la petición a la relación M–N panel<–>caregiver.
    3) Devuelve {"assigned": true} si el panel existe y tiene paciente.
       En caso contrario {"assigned": false}.
    """
    # 1) Recuperar el panel
    panel = Panels.query.get(device_id)
    if not panel or panel.patient_id is None:
        return jsonify({'assigned': False}), 200

    # 2) Recoger el caregiver del token y asociarlo si no lo está ya
    caregiver_id = get_jwt_identity()
    caregiver = Caregivers.query.get(caregiver_id)
    if not caregiver:
        abort(404, "Cuidador no encontrado")

    if caregiver not in panel.caregivers:
        panel.caregivers.append(caregiver)
        # commit puede dispararse automáticamente por autoflush,
        # pero lo dejamos explícito:
        db.session.commit()

    # 3) Siempre devolvemos assigned: true porque el panel ya existía y tenía paciente
    return jsonify({'assigned': True}), 200

@panels_bp.route("/<string:device_id>/assign", methods=["POST"])
@jwt_required(locations=["cookies"])
def assign_panel(device_id):
    """
    Asigna o actualiza un panel:
      - device_id → PK en la tabla panels
      - name      → ahora lo leemos de body JSON (fallback: device_id)
    Body JSON: {
      "patient_id":  123,
      "caregiver_id":77,
      "name":       "Panel Sala A"    # <-- nuevo campo opcional
    }
    """
    data = request.get_json(silent=True) or {}
    pid  = data.get("patient_id")
    cid  = data.get("caregiver_id")
    panel_name = data.get("name", device_id)   # <— aquí

    if pid is None or cid is None:
        abort(400, "patient_id y caregiver_id requeridos")

    now = datetime.utcnow()
    panel = Panels.query.get(device_id)

    if not panel:
        # Creamos panel por primera vez,
        # usando el name que venga en JSON (o device_id si no lo mandaron)
        panel = Panels(
            device_id           = device_id,
            name                = panel_name,         # <— usamos panel_name
            patient_id          = pid,
            last_seen           = now,
            created_at          = now
        )
        db.session.add(panel)
    else:
        # Si ya existía, actualizamos el name (si cambió),
        # y paciente/timestamp
        panel.name                = panel_name    # <— actualizamos name
        panel.patients_patient_id = pid
        panel.last_seen           = now

    # Asignamos el cuidador (si no lo tenía)
    caregiver = Caregivers.query.get(cid)
    if not caregiver:
        abort(404, "Cuidador no encontrado")

    if caregiver not in panel.caregivers:
        panel.caregivers.append(caregiver)

    db.session.commit()
    return jsonify({"status": "assigned"}), 200