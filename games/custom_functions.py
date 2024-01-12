# custom_functions.py
from .models import Game

def get_games_by_genre(genre):
    return Game.objects.filter(genre=genre)
