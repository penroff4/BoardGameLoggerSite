from django.urls import path

from . import views

urlpatterns = [
        # ex: /games/
        path('', views.index, name='index'),

        # ex: /games/1/
        path('<int:game_id>/', views.gameDetail, name='detail'),
        ]
