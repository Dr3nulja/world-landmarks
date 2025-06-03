from flask import request, jsonify
from app.models.landmark import Landmark
from app.extensions import db
from flask_jwt_extended import get_jwt_identity
from app.models.user import User

def create_landmark():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    location = data.get("location")
    country = data.get("country")

    user_id = get_jwt_identity()
    new_landmark = Landmark(
        name=name,
        description=description,
        location=location,
        country=country,
        user_id=user_id
    )

    db.session.add(new_landmark)
    db.session.commit()

    return jsonify({"message": "Landmark created successfully"}), 201

def get_all_landmarks():
    country = request.args.get("country")
    sort_by_rating = request.args.get("rating")

    query = Landmark.query

    if country:
        query = query.filter_by(country=country)

    landmarks = query.all()

    results = [
        {
            "id": l.id,
            "name": l.name,
            "description": l.description,
            "location": l.location,
            "country": l.country,
            "user_id": l.user_id
        } for l in landmarks
    ]

    return jsonify(results)

def get_landmark_by_id(landmark_id):
    landmark = Landmark.query.get_or_404(landmark_id)
    return jsonify({
        "id": landmark.id,
        "name": landmark.name,
        "description": landmark.description,
        "location": landmark.location,
        "country": landmark.country,
        "user_id": landmark.user_id
    })

def update_landmark(landmark_id):
    user_id = get_jwt_identity()
    landmark = Landmark.query.get_or_404(landmark_id)

    if landmark.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    landmark.name = data.get("name", landmark.name)
    landmark.description = data.get("description", landmark.description)
    landmark.location = data.get("location", landmark.location)
    landmark.country = data.get("country", landmark.country)

    db.session.commit()
    return jsonify({"message": "Landmark updated"})

def delete_landmark(landmark_id):
    user_id = get_jwt_identity()
    landmark = Landmark.query.get_or_404(landmark_id)

    if landmark.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(landmark)
    db.session.commit()
    return jsonify({"message": "Landmark deleted"})
