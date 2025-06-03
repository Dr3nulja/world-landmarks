from app import db

class Rating(db.Model):
    __tablename__ = 'ratings'

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmarks.id'), nullable=False)

    def __repr__(self):
        return f"<Rating {self.score} for landmark {self.landmark_id}>"
