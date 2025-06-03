from flask import Blueprint
from app.controllers.rating_controller import (
    add_rating, update_rating, delete_rating, get_average_rating
)
from flask_jwt_extended import jwt_required

rating_bp = Blueprint('rating_bp', __name__)

rating_bp.route('', methods=['POST'])(jwt_required()(add_rating))
rating_bp.route('/<int:rating_id>', methods=['PUT'])(jwt_required()(update_rating))
rating_bp.route('/<int:rating_id>', methods=['DELETE'])(jwt_required()(delete_rating))
rating_bp.route('/landmark/<int:landmark_id>', methods=['GET'])(get_average_rating)
