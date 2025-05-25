from flask import Blueprint, abort, jsonify, request
from ..services.alerts_service import get_all_alerts, create_alert_by_button, fetch_active_alerts_by_caregiver
from ..models.panels import Panels
from flask_jwt_extended import jwt_required

alerts_bp = Blueprint('alerts', __name__, url_prefix='/api/alerts')

@alerts_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_alerts():
    alerts = get_all_alerts()
    return jsonify([{'alert_id': a.alert_id, 'alert_type': a.alert_type, 'description': a.description, 'patients_patient_id': a.patients_patient_id} for a in alerts])

@alerts_bp.route('/active/<int:caregiver_id>', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_alerts_by_caregiver(caregiver_id):
    data = fetch_active_alerts_by_caregiver(caregiver_id)
    return jsonify(data)

@alerts_bp.route("/patients/<int:patient_id>/<int:button_id>", methods=["POST"])
@jwt_required(locations=['cookies'])
def add_alert(patient_id, button_id):
    state = int(request.get_json(silent=True).get("state", 1))

    if button_id not in range(0, 7):
        abort(400, "button_id fuera de rango")

    # identifica panel y cuidador automáticamente
    panel = Panels.query.filter_by(patient_id=patient_id).first()
    if not panel:
        abort(404, "panel no asignado a ese paciente")

    alert = create_alert_by_button(button_id, state, panel)
    return jsonify({
        "alert_id": alert.alert_id,
        "alert_type": alert.alert_type,
        "state": alert.state,
    }), 201