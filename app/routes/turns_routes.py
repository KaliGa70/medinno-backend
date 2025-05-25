from flask import Blueprint, jsonify, request
from ..services.turns_service import get_all_turns, create_turn
from flask_jwt_extended import jwt_required

turns_bp = Blueprint('turns', __name__, url_prefix='/api/turns')

@turns_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_turns():
    turns = get_all_turns()
    return jsonify([{'turn_id': t.turn_id, 'description': t.description} for t in turns])

@turns_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_turn():
    data = request.get_json()
    new_turn = create_turn(data)
    return jsonify({'message': 'Turn created successfully', 'turn_id': new_turn.turn_id}), 201