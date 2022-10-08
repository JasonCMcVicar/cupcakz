"""Flask app for Cupcakes"""

import re
from flask import Flask, request, redirect, render_template, jsonify
# from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nope'

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///cupcakz"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

@app.get('/api/cupcakes')
def list_cupcakes():
    """List all cupcakes.

    Return: {cupcakes: [{id, flavor, size, rating, image}, ...]}
    """
    cupcake_instances = Cupcake.query.all()
    cupcakes = []

    for cupcake in cupcake_instances:
        cupcakes.append(cupcake.serialize())

    return jsonify(cupcakes=cupcakes)

@app.get('/api/cupcakes/<int:cupcake_id>')
def list_cupcake(cupcake_id):
    """List a single cupcake.

    Return: {cupcake: {id, flavor, size, rating, image}}
    """
    cupcake_instance = Cupcake.query.get_or_404(cupcake_id)
    cupcake_instance = cupcake_instance.serialize()

    return jsonify(cupcake=cupcake_instance)

@app.post('/api/cupcakes')
def add_cupcake():
    """Create a new cupcake with flavor, size, rating, and image.

    Return: {cupcake: {id, flavor, size, rating, image}}
    """
    flavor = request.json["flavor"]
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']
    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()

    cupcake = cupcake.serialize()

    return (jsonify(cupcake=cupcake), 201)

@app.patch('/api/cupcakes/<int:cupcake_id>')
def update_cupcake(cupcake_id):
    """Update an existing cupcake with flavor, size, rating, and/or image

    Return: {cupcake: {id, flavor, size, rating, image}}
    """
    cupcake_instance = Cupcake.query.get_or_404(cupcake_id)
    # flavor = request.json.get("flavor", cupcake_instance.flavor)
    flavor = request.json.get("flavor", None)
    size = request.json.get("size", cupcake_instance.size)
    rating = request.json.get("rating", cupcake_instance.rating)
    image = request.json.get("image", cupcake_instance.image)

    # cupcake_instance.flavor = flavor
    cupcake_instance.flavor = flavor if flavor != None else cupcake_instance.flavor

    cupcake_instance.size = size
    cupcake_instance.rating = rating
    cupcake_instance.image = image

    db.session.commit()

    cupcake = cupcake_instance.serialize()

    return jsonify(cupcake=cupcake)
