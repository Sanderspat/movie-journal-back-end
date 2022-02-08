from flask import Flask 
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongodb_client = PyMongo(app)
db = mongodb_client.db

from .routes import movies_bp
app.register_blueprint(movies_bp)