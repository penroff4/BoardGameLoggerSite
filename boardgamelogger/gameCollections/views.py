from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

from .models import gameCollection

def index(request):
    
    latest_game_collections_list = gameCollection.objects.order_by('-collection_started_date')[:5]

    # template = loader.get_template('gameCollections/index.html')
    context = {'latest_game_collections_list': latest_game_collections_list, }
    
    return render(request, 'gameCollections/index.html', context)

def gameDetail(request, game_id):
    return HttpResponse("You're looking at game %s." % game_id)

def gameCollectionView(request, collection_id):
    return HttpResponse("You're looking at collection %s." % collection_id)
