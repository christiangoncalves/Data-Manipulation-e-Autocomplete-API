from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Timeline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String)
    timestamp = db.Column(db.String)
