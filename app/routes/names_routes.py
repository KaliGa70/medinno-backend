from flask import Blueprint, jsonify, request
from ..services.names_service import get_all_names, create_name

names_bp = Blueprint('names', __name__)

@names_bp.route('/names', methods=['GET'])
def get_names():
    names = get_all_names()
    return jsonify([{'name_id': n.name_id, 'first_name': n.first_name, 'middle_name': n.middle_name, 'last_name': n.last_name, 'second_last_name': n.second_last_name} for n in names])

@names_bp.route('/names', methods=['POST'])
def add_name():
    data = request.get_json()
    new_name = create_name(data)
    return jsonify({'message': 'Name created successfully', 'name_id': new_name.name_id}), 201