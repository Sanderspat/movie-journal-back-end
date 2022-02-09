from app import db
from flask import Blueprint, jsonify, request 
from bson.objectid import ObjectId

movies_bp = Blueprint("movies",__name__,url_prefix="/movies")

#Movies
#insert-POST
@movies_bp.route("", methods=["POST"])
def post_movies():
    movies = db.movies.insert_one({ 'title': 'Mean Girls', 'year_released':'2004','my_rating':'10','thoughts':'Another Cult Classic' })

    return jsonify('Added Movie'),201

# READ-GET
@movies_bp.route("/1",methods=["GET"])
def get_movie():

    movie = db.movies.find_one({"_id":ObjectId("6201c8ab278a994a08504ab2")})
    movie['_id'] = str(movie['_id'])

    print(movie)
    return jsonify(movie), 200

#FIND-ALL
@movies_bp.route("",methods=["GET"])
def get_movies():

    movies = db.movies.find()
    movies = list(movies)
    movieList = []
    for movie in movies:
        movie['_id'] = str(movie['_id'])
        movieList.append(movie)
    
    return jsonify(movieList),200

#UPDATE-PUT-ONE
@movies_bp.route("/edit",methods=["PUT"])
def put_movie():
    movie = db.movies.update_one({"_id":ObjectId("6201c8ab278a994a08504ab2")},{'title': 'Con Air'})
    movie['_id'] = str(movie['_id'])

    print(movie) 

# #DELETE-DELETE_ONE
# @movies_bp.route("",methods=["DELETE"])
# def delete_movies():
#     movies = db.movies.delete_one({'_id': moviesId})


