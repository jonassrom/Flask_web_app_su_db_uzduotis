from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Automobilis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gamintojas = db.Column(db.String(50), nullable=False)
    modelis = db.Column(db.String(50), nullable=False)
    spalva = db.Column(db.String(30), nullable=False)
    metai = db.Column(db.Integer, nullable=False)
    kaina = db.Column(db.Float, nullable=False)
