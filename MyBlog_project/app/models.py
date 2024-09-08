from flask_sqlalchemy import SQLAlchemy
from flask import url_for

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ ='posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(50), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'), nullable=True)

    def __str__(self):
        return f"{self.title}"

    @property
    def image_url(self):
        return url_for('static', filename=f"posts/images/{self.image}")

    @property
    def show_url(self):
        return url_for('posts.show', id=self.id)

    @property
    def delete_url(self):
        return url_for('posts.delete', id=self.id)

    @property
    def edit_url(self):
        return url_for('posts.edit', id=self.id)


class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='accounts', lazy=True)

    def __str__(self):
        return f"{self.f_name}"

    @property
    def show_url(self):
        return url_for('accounts.show', id=self.id)
