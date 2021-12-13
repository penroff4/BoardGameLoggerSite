from django.shortcuts import render, get_object_or_404

from .models import Game

def index(request):
    
    latest_games_list = Game.objects.order_by('-game_added_date')[:5]

    context = {'latest_games_list': latest_games_list, }
    
    return render(request, 'games/index.html', context)

def gameDetail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)

    return render(request, 'games/detail.html', {'game': game})
