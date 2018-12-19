from flask import Flask
from instance import config

def create_app(config_name="development_config"):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.config[config_name])
    return app