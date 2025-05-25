from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    get_csrf_token
)
from ..services.caregivers_service import CaregiverAuthService, get_all_caregivers, get_caregiver_profile

caregivers_bp = Blueprint('caregivers_bp', __name__, url_prefix='/api/caregivers')


@caregivers_bp.route('', methods=['GET'])
@jwt_required(locations=['cookies'])
def get_caregivers():
    caregivers = get_all_caregivers()
    return jsonify([{'caregiver_id': c.caregiver_id, 'password': c.password, 'email': c.email, 'name_id': c.name_id} for c in caregivers])

@caregivers_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    try:
        caregiver = CaregiverAuthService.register_caregiver(
            email=data.get('email', '').strip(),
            password=data.get('password', ''),
            name_id=data.get('name_id')
        )
    except ValueError as e:
        return jsonify(msg=str(e)), 409

    access_token  = create_access_token(identity=str(caregiver.caregiver_id))
    refresh_token = create_refresh_token(identity=str(caregiver.caregiver_id))

    resp = make_response(jsonify(
        msg='Caregiver registrado',
        access_csrf  = get_csrf_token(access_token),
        refresh_csrf = get_csrf_token(refresh_token)
    ), 201)
    set_access_cookies(resp,  access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp

@caregivers_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    caregiver = CaregiverAuthService.authenticate(
        email=data.get('email', '').strip(),
        password=data.get('password', '')
    )
    if not caregiver:
        return jsonify(msg='Credenciales inválidas'), 401

    access_token  = create_access_token(identity=str(caregiver.caregiver_id))
    refresh_token = create_refresh_token(identity=str(caregiver.caregiver_id))

    resp = make_response(jsonify(
        msg='Login exitoso',
        access_csrf  = get_csrf_token(access_token),
        refresh_csrf = get_csrf_token(refresh_token)
    ), 200)
    set_access_cookies(resp,  access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp

@caregivers_bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True, locations=['cookies'])
def refresh():
    user_id    = get_jwt_identity()
    new_access = create_access_token(identity=str(user_id))

    resp = make_response(jsonify(
        access_csrf = get_csrf_token(new_access)
    ), 200)
    set_access_cookies(resp, new_access)
    return resp

@caregivers_bp.route('/logout', methods=['POST'])
def logout():
    resp = make_response(jsonify(msg='Logout exitoso'), 200)
    unset_jwt_cookies(resp)
    return resp

@caregivers_bp.route('/me', methods=['GET'])
@jwt_required(locations=['cookies'])
def me():
    profile = get_caregiver_profile(get_jwt_identity())
    if not profile:
        return jsonify(msg='Caregiver no encontrado'), 404
    return jsonify(profile), 200
