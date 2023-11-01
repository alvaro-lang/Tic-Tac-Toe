
from django.db import models

class Player(models.Model):

    name = models.CharField(max_length=30)
    gamesWon = models.IntegerField(default=0)

    class Meta:
        db_table = 'player'