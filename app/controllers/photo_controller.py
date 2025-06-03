from flask import request, jsonify
from app.extensions import db
from app.models.photo import Photo
from flask_jwt_extended import get_jwt_identity

def upload_photo():
    data = request.get_json()
    image_url = data.get("image_url")
    landmark_id = data.get("landmark_id")

    new_photo = Photo(
        image_url=image_url,
        user_id=get_jwt_identity(),
        landmark_id=landmark_id
    )

    db.session.add(new_photo)
    db.session.commit()

    return jsonify({"message": "Photo uploaded successfully"}), 201

def get_photos_by_landmark(landmark_id):
    photos = Photo.query.filter_by(landmark_id=landmark_id).all()
    result = [{"id": p.id, "image_url": p.image_url, "user_id": p.user_id} for p in photos]
    return jsonify(result)

def delete_photo(photo_id):
    photo = Photo.query.get_or_404(photo_id)
    if photo.user_id != get_jwt_identity():
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(photo)
    db.session.commit()
    return jsonify({"message": "Photo deleted successfully"})
