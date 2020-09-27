from flask import render_template, request, redirect
from app import app
#! from app.models.game import battle
#! from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

#! @app.route('/<choice_1>/<choice_2>', methods=['POST'])
#! def play_rps():
