import datetime

from django.db import models
from django.utils import timezone

from gameCollections.models import gameCollection


class Game(models.Model):
    game_collection = models.ForeignKey(
            gameCollection,
            on_delete=models.CASCADE)
    game_title = models.CharField(max_length=200)
    game_publisher = models.CharField(max_length=200)
    game_bgg_url = models.CharField(max_length=200)
    game_pub_date = models.DateTimeField('date published', blank=True)
    game_added_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def __str__(self):
        return self.game_title

    def was_added_recently(self):
        return self.game_added_date >= timezone.now() - datetime.timedelta(days=1)


