from flask import Flask,Blueprint
from instance import config
#local imports
from app.api.books.v1 import library_v1
from app.api.books.v2 import library_v2
from app.api.users.v1 import users_v1
from app.api.users.v2 import users_v2

def create_app(config_name="testing_config"):
    """
    Method to create the app
    """
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.config[config_name])
    app.register_blueprint(library_v1)
    app.register_blueprint(library_v2)
    app.register_blueprint(users_v1)
    app.register_blueprint(users_v2)
    return app

