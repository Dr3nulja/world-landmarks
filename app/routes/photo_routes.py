from flask import Blueprint
from app.controllers.photo_controller import (
    upload_photo, get_photos_by_landmark, delete_photo
)
from flask_jwt_extended import jwt_required

photo_bp = Blueprint('photo_bp', __name__)

photo_bp.route('', methods=['POST'])(jwt_required()(upload_photo))
photo_bp.route('/<int:landmark_id>', methods=['GET'])(get_photos_by_landmark)
photo_bp.route('/<int:photo_id>', methods=['DELETE'])(jwt_required()(delete_photo))
