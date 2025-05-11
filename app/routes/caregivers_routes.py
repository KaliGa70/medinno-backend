from flask import Blueprint, jsonify, request
from ..services.caregivers_service import get_all_caregivers, create_caregiver

caregivers_bp = Blueprint('caregivers', __name__)

@caregivers_bp.route('/caregivers', methods=['GET'])
def get_caregivers():
    caregivers = get_all_caregivers()
    return jsonify([{'caregiver_id': c.caregiver_id, 'password': c.password, 'email': c.email, 'name_id': c.name_id} for c in caregivers])

@caregivers_bp.route('/caregivers', methods=['POST'])
def add_caregiver():
    data = request.get_json()
    new_caregiver = create_caregiver(data)
    return jsonify({'message': 'Caregiver created successfully', 'caregiver_id': new_caregiver.caregiver_id}), 201