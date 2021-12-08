from django.urls import path

from . import views

urlpatterns = [
        # ex: /gamecollections/
        path('', views.index, name='index'),

        # ex: /gameCollections/1/
        path('<int:collection_id>/', views.gameCollectionView, name='detail'),
        ]
