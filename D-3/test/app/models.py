from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from sqlalchemy.orm import lazyload

db = SQLAlchemy()


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    grade = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=True)


    def __str__(self):
        return f'{self.name}'

    @property
    def image_url(self):
        return url_for('static', filename=f"students/images/{self.image}")

    @property
    def show_url(self):
        return url_for('students.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('students.delete', id=self.id)

    @property
    def edit_url(self):
        return url_for('students.edit', id=self.id)


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    students= db.relationship('Student', backref='track', lazy=True)

    def __str__(self):
        return self.name

    @property
    def show_url(self):
        return url_for('tracks.show', id=self.id)
