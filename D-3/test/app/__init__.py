from flask import Flask
from flask_migrate import Migrate
from app.config import config_options
from app.models import db

def create_app(config_name='prd'):
    app = Flask(__name__)
    current_config = config_options[config_name]
    app.config.from_object(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI

    db.init_app(app)

    migrate = Migrate(app, db)

    from app.students import student_blueprint
    app.register_blueprint(student_blueprint)

    from app.tracks import track_blueprint
    app.register_blueprint(track_blueprint)

    return app

