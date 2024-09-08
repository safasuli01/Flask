from flask_restful import Resource, marshal_with
from app.models import db, Post
from app.posts.api.serializers import post_serializers
from app.posts.api.parsers import post_parser

class PostList(Resource):
    @marshal_with(post_serializers)
    def get(self):
        posts = Post.query.all()
        return posts, 200

    @marshal_with(post_serializers)
    def post(self):
        post_args = post_parser.parse_args()
        post = Post(**post_args)
        db.session.add(post)
        db.session.commit()
        return post, 201

class PostResource(Resource):
    @marshal_with(post_serializers)
    def get(self, id):
        post = db.get_or_404(Post, id)
        return post, 200

    @marshal_with(post_serializers)
    def put(self, id):
        post = db.get_or_404(Post, id)
        post_args = post_parser.parse_args()
        post.title = post_args['title']
        post.description = post_args['description']
        post.image = post_args['image']
        post.account_id = post_args['account_id']
        db.session.commit()
        return post, 200

    def delete(self, id):
        post = db.get_or_404(Post, id)
        db.session.delete(post)
        db.session.commit()
        return '', 204
