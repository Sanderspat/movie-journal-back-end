from app import db
from flask import Blueprint, jsonify, request 

movies_bp = Blueprint("movies",__name__,url_prefix="/movies")

#Movies
#insert-POST
@movies_bp.route("", methods=["POST"])
def post_movies():
    movies = db.movies.insert_one({ 'title': 'Mean Girls', 'year_released':'2004','my_rating':'10','thoughts':'Another Cult Classic' })

    return jsonify('Added Movie'),201

#READ-GET
# @movies_bp.route("",methods=["GET"])
# def get_movies():
#     # movies = db.movies.find({'id':'1'})

#     return jsonify(movies), 200

#UPDATE-PUT
@movies_bp.route("",methods=["PUT"])
def put_movies():
    movies = db.movies.update_one({'_id': 1},{'title': 'Con Air'})

    return{}