from flask import Blueprint, jsonify, request
from ..services.patients_service import get_all_patients, create_patient, get_all_patients_by_caregiver, get_all_patients_by_caregiver_count
from ..services.panels_service import PanelsService
from flask_jwt_extended import jwt_required
from .. import db

patients_bp = Blueprint('patients', __name__, url_prefix='/api/patients')

@patients_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_patients():
    patients = get_all_patients()
    return jsonify([{'patient_id': p.patient_id, 'cuarto': p.cuarto, 'fecha_nacimiento': p.fecha_nacimiento, 'sexo': p.sexo, 'name_id': p.name_id} for p in patients])

@patients_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_patient():
    data = request.get_json()
    new_patient = create_patient(data)
    return jsonify({'message': 'Patient created successfully', 'patient_id': new_patient.patient_id}), 201


@patients_bp.route('/stats/<int:caregiver_id>', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_patients_stats(caregiver_id):
    # Obtén los pacientes asignados a este cuidador (debes implementar esta función)
    patients = get_all_patients_by_caregiver_count(caregiver_id)
    total_patients = len(patients)

    # Instancia servicio con la sesión actual
    service = PanelsService(db.session)
    panels_activos_count = service.count_active_panels_for_caregiver(caregiver_id)

    stats = [
        {"title": "Total Pacientes", "value": total_patients, "icon": "peopleOutline"},
        {"title": "Panels Activos", "value": panels_activos_count, "icon": "clipboardOutline"},
    ]

    return jsonify(stats)

@patients_bp.route('/getByCaregiver/<int:caregiver_id>', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_patients_byCaregiver(caregiver_id):
    patients = get_all_patients_by_caregiver(caregiver_id)
    if not patients:
        return jsonify(msg='Patients no encontrados'), 404
    return jsonify(patients), 200
