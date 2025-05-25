from flask import Blueprint, jsonify, request
from ..services.names_service import get_all_names, create_name
from flask_jwt_extended import jwt_required

names_bp = Blueprint('names', __name__, url_prefix='/api/names')

@names_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_names():
    names = get_all_names()
    return jsonify([{'name_id': n.name_id, 'first_name': n.first_name, 'middle_name': n.middle_name, 'last_name': n.last_name, 'second_last_name': n.second_last_name} for n in names])

@names_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_name():
    data = request.get_json()
    new_name = create_name(data)
    return jsonify({'message': 'Name created successfully', 'name_id': new_name.name_id}), 201