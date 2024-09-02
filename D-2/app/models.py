from flask import url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    image = db.Column(db.String(250))
    description = db.Column(db.String(250))

    def __str__(self):
        return f"{self.name}"
    @property
    def image_url(self):
        return url_for("static", filename=f"images/{self.image}")

    @property
    def show_url(self):
        return url_for("show", id=self.id)

    @property
    def delete_url(self):
        return url_for("delete", post=self.id)