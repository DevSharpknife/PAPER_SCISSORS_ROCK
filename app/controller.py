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

@app.route('/<choice_1>/<choice_2>', methods=['POST'])
def play_rps():
    player_1 = Player(request.form['P1_name'], request.form['P1_choice'])
    player_2 = Player(request.form['P2_name'], request.form['P2_choice'])
    game = Game()
    fight_card = game.fight(player_1, player_2)
    
    return render_template('battle.html', fight_card=fight_card)
