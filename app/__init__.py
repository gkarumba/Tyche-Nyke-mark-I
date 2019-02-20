from flask import Flask,Blueprint
from instance import config
from flask_cors import CORS
#local imports
from app.api.books.v1 import library_v1
from app.api.books.v2 import library_v2
from app.api.users.v1 import users_v1
from app.api.users.v2 import users_v2
from app.database.database import BooksDB

db = BooksDB()

def create_app(config_name="development_config"):
    """
    Method to create the app
    """
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_object(config.config[config_name])
    CORS(app)
    db.create_tables()
    db.create_users_table()
    db.create_borrow_table()
    app.register_blueprint(library_v1)
    app.register_blueprint(library_v2)
    app.register_blueprint(users_v1)
    app.register_blueprint(users_v2)
    return app

