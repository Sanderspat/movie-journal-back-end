from flask import Blueprint

from .extensions import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    movie_collection = mongo.db.Test 
    movie_collection.insert({'title':'Lion King'})
    return '<h1> Added a User</h1>'