from flask import Blueprint, jsonify, request
from ..services.drugs_service import get_all_drugs, create_drug
from flask_jwt_extended import jwt_required

drugs_bp = Blueprint('drugs', __name__, url_prefix='/api/drugs')

@drugs_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_drugs():
    drugs = get_all_drugs()
    return jsonify([{'drug_id': d.drug_id, 'name': d.name, 'formato': d.formato, 'recipes_recipe_id': d.recipes_recipe_id} for d in drugs])

@drugs_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_drug():
    data = request.get_json()
    new_drug = create_drug(data)
    return jsonify({'message': 'Drug created successfully', 'drug_id': new_drug.drug_id}), 201