from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    time = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255))

    def __init__(self, title, description, time, image=None):
        self.title = title
        self.description = description
        self.time = time
        self.image = image

    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'time': self.time,
            'image': self.image
        }
