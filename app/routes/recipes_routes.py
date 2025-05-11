from flask import Blueprint, jsonify, request
from ..services.recipes_service import get_all_recipes, create_recipe

recipes_bp = Blueprint('recipes', __name__)

@recipes_bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = get_all_recipes()
    return jsonify([{'recipe_id': r.recipe_id, 'description': r.description, 'patients_patient_id': r.patients_patient_id} for r in recipes])

@recipes_bp.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.get_json()
    new_recipe = create_recipe(data)
    return jsonify({'message': 'Recipe created successfully', 'recipe_id': new_recipe.recipe_id}), 201