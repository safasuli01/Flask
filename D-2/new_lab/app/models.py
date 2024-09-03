from fileinput import filename

from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()


class Post (db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(100))
    description = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.title}'

    @property
    def image_url(self):
        return url_for('static' , filename=f"posts/images/{self.image}")

    @property
    def show_url(self):
        return url_for('posts.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('posts.delete', id=self.id)

    @property
    def edit_url(self):
        return url_for('posts.edit', id=self.id)