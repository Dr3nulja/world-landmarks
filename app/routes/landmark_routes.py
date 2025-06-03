from flask import Blueprint
from app.controllers.landmark_controller import (
    create_landmark, get_all_landmarks,
    get_landmark_by_id, update_landmark, delete_landmark
)
from flask_jwt_extended import jwt_required

landmark_bp = Blueprint('landmark_bp', __name__)

landmark_bp.route('', methods=['POST'])(jwt_required()(create_landmark))
landmark_bp.route('', methods=['GET'])(get_all_landmarks)
landmark_bp.route('/<int:landmark_id>', methods=['GET'])(get_landmark_by_id)
landmark_bp.route('/<int:landmark_id>', methods=['PUT'])(jwt_required()(update_landmark))
landmark_bp.route('/<int:landmark_id>', methods=['DELETE'])(jwt_required()(delete_landmark))
