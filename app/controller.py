from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='Home')

# @app.route('/<choice_1>/<choice_2>', methods=['POST'])
# def play_rps():
    