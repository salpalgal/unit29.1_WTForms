from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    def __repr__(self):
        pet =self
        return f"<User {pet.id} {pet.name} {pet.species} {pet.photo_url} {pet.age} {pet.notes} {pet.available}>"

    id = db.Column(db.Integer, primary_key= True, autoincrement = True)
    name = db.Column(db.String(30),nullable = False)
    species = db.Column(db.String(30), nullable = False)
    photo_url = db.Column(db.String, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.String, nullable =True)
    available = db.Column(db.Boolean, default = True)
