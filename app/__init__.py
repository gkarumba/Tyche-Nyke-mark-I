from flask import Flask,Blueprint
from instance import config
#local imports
from app.api.books.v1 import bk1

def create_app(config_name="development_config"):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.config[config_name])
    app.register_blueprint(bk1)
    return app