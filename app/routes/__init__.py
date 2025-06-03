from .auth_routes import auth_bp
from .landmark_routes import landmark_bp
from .photo_routes import photo_bp
from .rating_routes import rating_bp

all_blueprints = [
    (auth_bp, "/api/auth"),
    (landmark_bp, "/api/landmarks"),
    (photo_bp, "/api/photos"),
    (rating_bp, "/api/ratings"),
]
