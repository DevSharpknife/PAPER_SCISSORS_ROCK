from flask import render_template, request, redirect
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='A WORLD OF PAIN!!!')

@app.route('/battle')
def battle():
    return render_template('battle.html', title='READY FOR BATTLE?')

@app.route('/result', methods=['GET','POST'])
def result():
    player_1 = Player(request.form['P1_name'], request.form['P1_choice'])
    player_2 = Player(request.form['P2_name'], request.form['P2_choice']) 
    game = Game(player_1, player_2)
    fight_card = game.fight()
    return render_template('result.html', fight_card=fight_card)
