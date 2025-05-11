from flask import Blueprint, jsonify, request
from ..services.turns_service import get_all_turns, create_turn

turns_bp = Blueprint('turns', __name__)

@turns_bp.route('/turns', methods=['GET'])
def get_turns():
    turns = get_all_turns()
    return jsonify([{'turn_id': t.turn_id, 'description': t.description} for t in turns])

@turns_bp.route('/turns', methods=['POST'])
def add_turn():
    data = request.get_json()
    new_turn = create_turn(data)
    return jsonify({'message': 'Turn created successfully', 'turn_id': new_turn.turn_id}), 201