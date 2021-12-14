from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
        # ex: /games/
        path('', views.index, name='index'),

        # ex: /games/1/
        path('<int:game_id>/', views.gameDetail, name='detail'),

        # ex: /games/1/vote
        path('<int:game_id>/vote/', views.vote,name='vote'),
        ]
