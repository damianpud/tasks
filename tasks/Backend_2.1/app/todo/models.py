from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=128), nullable=False)
    description = db.Column(db.String(length=5000))
    created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'{super().__repr__()}: {self.title}'

