from flask import Flask
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api

from app.config import config_options
from app.models import db


def create_app(config_name='prd'):
    app = Flask(__name__)
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)
    api = Api(app)

    from app.posts import post_blueprint
    app.register_blueprint(post_blueprint)

    from app.accounts import account_blueprint
    app.register_blueprint(account_blueprint)

    ##genertating api
    from app.posts.api.views import PostList
    api.add_resource(PostList, '/api/posts')

    return app
