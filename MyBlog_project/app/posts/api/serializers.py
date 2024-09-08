from flask_restful import fields

account_serializer = {
    "id": fields.Integer,
    "f_name": fields.String,
    "l_name": fields.String,
    "mail": fields.String,
}

post_serializers = {
    "id": fields.Integer,
    "title": fields.String,
    "image": fields.String,
    "description": fields.String,
    "account_id": fields.Integer,
    "account": fields.Nested(account_serializer),
}
