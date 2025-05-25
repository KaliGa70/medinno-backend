from flask import Blueprint, jsonify, request
from ..services.medication_schedules_service import get_all_medication_schedules, create_medication_schedule
from flask_jwt_extended import jwt_required

medication_schedules_bp = Blueprint('medication_schedules', __name__, url_prefix='/api/medication-schedules')

@medication_schedules_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_medication_schedules():
    schedules = get_all_medication_schedules()
    return jsonify([{'medication_schedule_id': s.medication_schedule_id, 'fecha': s.fecha, 'hora': s.hora, 'recipes_recipe_id': s.recipes_recipe_id} for s in schedules])

@medication_schedules_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_medication_schedule():
    data = request.get_json()
    new_schedule = create_medication_schedule(data)
    return jsonify({'message': 'Medication schedule created successfully', 'medication_schedule_id': new_schedule.medication_schedule_id}), 201