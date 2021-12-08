from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

from .models import Game

def index(request):
    
    latest_games_list = Game.objects.order_by('-game_added_date')[:5]

    context = {'latest_games_list': latest_games_list, }
    
    return render(request, 'games/index.html', context)

def gameDetail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)