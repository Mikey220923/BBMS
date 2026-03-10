from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    blood_group = db.Column(db.String(10), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    city = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Donor {self.name} - {self.blood_group}>"
