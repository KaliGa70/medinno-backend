from flask import Blueprint, jsonify, request
from ..services.patients_service import get_all_patients, create_patient

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['GET'])
def get_patients():
    patients = get_all_patients()
    return jsonify([{'patient_id': p.patient_id, 'cuarto': p.cuarto, 'fecha_nacimiento': p.fecha_nacimiento, 'sexo': p.sexo, 'name_id': p.name_id} for p in patients])

@patients_bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = create_patient(data)
    return jsonify({'message': 'Patient created successfully', 'patient_id': new_patient.patient_id}), 201