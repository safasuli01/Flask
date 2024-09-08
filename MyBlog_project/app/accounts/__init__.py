

from flask import Blueprint

account_blueprint = Blueprint('accounts', __name__, url_prefix='/accounts')
from app.accounts import views
