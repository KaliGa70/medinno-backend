from flask import Blueprint, jsonify, request
from ..services.drugs_service import get_all_drugs, create_drug

drugs_bp = Blueprint('drugs', __name__)

@drugs_bp.route('/drugs', methods=['GET'])
def get_drugs():
    drugs = get_all_drugs()
    return jsonify([{'drug_id': d.drug_id, 'name': d.name, 'formato': d.formato, 'recipes_recipe_id': d.recipes_recipe_id} for d in drugs])

@drugs_bp.route('/drugs', methods=['POST'])
def add_drug():
    data = request.get_json()
    new_drug = create_drug(data)
    return jsonify({'message': 'Drug created successfully', 'drug_id': new_drug.drug_id}), 201