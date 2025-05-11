from flask import Blueprint, jsonify, request
from ..services.medication_schedules_service import get_all_medication_schedules, create_medication_schedule

medication_schedules_bp = Blueprint('medication_schedules', __name__)

@medication_schedules_bp.route('/medication-schedules', methods=['GET'])
def get_medication_schedules():
    schedules = get_all_medication_schedules()
    return jsonify([{'medication_schedule_id': s.medication_schedule_id, 'fecha': s.fecha, 'hora': s.hora, 'recipes_recipe_id': s.recipes_recipe_id} for s in schedules])

@medication_schedules_bp.route('/medication-schedules', methods=['POST'])
def add_medication_schedule():
    data = request.get_json()
    new_schedule = create_medication_schedule(data)
    return jsonify({'message': 'Medication schedule created successfully', 'medication_schedule_id': new_schedule.medication_schedule_id}), 201