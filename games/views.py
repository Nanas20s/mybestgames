from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm  # You'll need to create a form for game creation


def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'games/game_create.html', {'form': form})

from .custom_functions import get_games_by_genre

def some_view(request):
    # Call the custom function to get games by genre
    action_games = get_games_by_genre('Action')
    # Do something with the games

def game_update(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

def game_delete(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})

def game_detail(request, id):
    game = get_object_or_404(Game, id=id)
    return render(request, 'games/game_detail.html', {'game': game})

def game_update(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_detail', id=game.id)
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

def game_delete(request, id):
    game = get_object_or_404(Game, id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})
