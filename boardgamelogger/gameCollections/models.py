from django.db import models

class gameCollection(models.Model):
    collection_name = models.CharField(max_length=200)
    collection_started_date = models.DateTimeField('date created', auto_now_add=True)
    # collection_owner
    # collection_num_gamesj
    # collection_most_recent_addition_date

    def __str__(self):
        return self.collection_name