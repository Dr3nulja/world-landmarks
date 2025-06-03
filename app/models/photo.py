from app import db

class Photo(db.Model):
    __tablename__ = 'photos'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    landmark_id = db.Column(db.Integer, db.ForeignKey('landmarks.id'), nullable=False)

    def __repr__(self):
        return f"<Photo {self.id} - {self.image_url}>"
