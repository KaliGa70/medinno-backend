from flask import Blueprint, jsonify, request
from ..services.recipes_service import get_all_recipes, create_recipe
from flask_jwt_extended import jwt_required

recipes_bp = Blueprint('recipes', __name__, url_prefix='/api/recipes')

@recipes_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_recipes():
    recipes = get_all_recipes()
    return jsonify([{'recipe_id': r.recipe_id, 'description': r.description, 'patients_patient_id': r.patients_patient_id} for r in recipes])

@recipes_bp.route('', methods=['POST'])
@jwt_required(locations=['cookies'])
def add_recipe():
    data = request.get_json()
    new_recipe = create_recipe(data)
    return jsonify({'message': 'Recipe created successfully', 'recipe_id': new_recipe.recipe_id}), 201