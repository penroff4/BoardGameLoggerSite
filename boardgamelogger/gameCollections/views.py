from django.shortcuts import render
from django.http import HttpResponse, Http404
# from django.template import loader

from .models import gameCollection

def index(request):
    
    latest_game_collections_list = gameCollection.objects.order_by('-collection_started_date')[:5]

    # template = loader.get_template('gameCollections/index.html')
    context = {'latest_game_collections_list': latest_game_collections_list, }
    
    return render(request, 'gameCollections/index.html', context)

def gameCollectionView(request, collection_id):
    try:
        collection = gameCollection.objects.get(pk=collection_id)
    except gameCollection.DoesNotExist:
        raise Http404("That game collection does not exist")
    return render(request, 'gameCollections/detail.html', {'collection': collection})
