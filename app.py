"""Flask app for Cupcakes"""

from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SECRET_KEY'] = "nope"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakz"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)
