from app import db

class Landmark(db.Model):
    __tablename__ = 'landmarks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    photos = db.relationship('Photo', backref='landmark', lazy=True)
    ratings = db.relationship('Rating', backref='landmark', lazy=True)

    def __repr__(self):
        return f"<Landmark {self.name}>"
