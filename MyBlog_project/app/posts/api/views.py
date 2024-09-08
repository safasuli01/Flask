from flask_restful import Resource, Api, marshal_with
from app.models import db, Post
from app.posts.api.serializers import post_serializers

#define class for the view

class PostList(Resource):
    @marshal_with(post_serializers)
    def get(self):
        posts = Post.query.all()
        return posts


    def post(self):
        pass