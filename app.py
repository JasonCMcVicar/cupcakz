"""Flask app for Cupcakes"""

import json
from flask import Flask, redirect, render_template, jsonify
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
