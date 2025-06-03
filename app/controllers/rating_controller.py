from flask import request, jsonify
from app.extensions import db
from app.models.rating import Rating
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import func

def add_rating():
    data = request.get_json()
    score = data.get("score")
    landmark_id = data.get("landmark_id")
    user_id = get_jwt_identity()

    existing = Rating.query.filter_by(user_id=user_id, landmark_id=landmark_id).first()
    if existing:
        return jsonify({"error": "You have already rated this landmark"}), 400

    new_rating = Rating(score=score, user_id=user_id, landmark_id=landmark_id)
    db.session.add(new_rating)
    db.session.commit()
    return jsonify({"message": "Rating added successfully"}), 201

def update_rating(rating_id):
    rating = Rating.query.get_or_404(rating_id)
    user_id = get_jwt_identity()

    if rating.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    rating.score = data.get("score", rating.score)
    db.session.commit()
    return jsonify({"message": "Rating updated"})

def delete_rating(rating_id):
    rating = Rating.query.get_or_404(rating_id)
    user_id = get_jwt_identity()

    if rating.user_id != user_id:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(rating)
    db.session.commit()
    return jsonify({"message": "Rating deleted"})

def get_average_rating(landmark_id):
    average = db.session.query(func.avg(Rating.score))\
        .filter(Rating.landmark_id == landmark_id).scalar()

    return jsonify({"landmark_id": landmark_id, "average_rating": round(average or 0, 2)})
