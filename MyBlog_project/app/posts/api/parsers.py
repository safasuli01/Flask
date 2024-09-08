from flask_restful import reqparse

post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True, help='Title is required')
post_parser.add_argument('image', type=str, help='Image is required')
post_parser.add_argument('description', type=str, required=True, help='Description is required')
post_parser.add_argument('account_id', type=int, required=True, help='Account ID is required')
