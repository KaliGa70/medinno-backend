from datetime import datetime
from flask import Blueprint, request, jsonify, abort
from ..models.panels import db, Panels

panels_bp = Blueprint("panels", __name__)

@panels_bp.route("/panels/<string:device_id>/config", methods=["GET"])
def get_config(device_id):
    """Lo consulta el ESP32 cada 30 s."""
    panel = Panels.query.get(device_id)
    if not panel or not panel.patient_id:
        return jsonify({"assigned": False}), 200

    panel.last_seen = datetime.utcnow()     # heartbeat
    db.session.commit()

    return jsonify({
        "assigned": True,
        "patient_id":   panel.patient_id,
        "caregiver_id": panel.caregiver_id,
    })

@panels_bp.route("/panels/<string:device_id>/assign", methods=["POST"])
def assign_panel(device_id):
    """
    Asigna (o crea) un panel escaneado por QR a paciente y cuidador.
    Espera JSON: { "patient_id": 123, "caregiver_id": 77 }
    """
    data = request.get_json(silent=True) or {}
    pid  = data.get("patient_id")
    cid  = data.get("caregiver_id")
    if pid is None or cid is None:
        abort(400, "patient_id y caregiver_id requeridos")

    now = datetime.utcnow()

    panel = Panels.query.get(device_id)
    if not panel:
        # Creamos con todos los campos NOT NULL cubiertos
        panel = Panels(
            device_id    = device_id,
            name         = device_id,   # evita NULL
            patient_id   = pid,
            caregiver_id = cid,
            last_seen    = now
        )
        db.session.add(panel)
    else:
        # Actualizamos asignación y heartbeat
        panel.patient_id   = pid
        panel.caregiver_id = cid
        panel.last_seen    = now

    db.session.commit()
    return jsonify({"status": "assigned"}), 200
