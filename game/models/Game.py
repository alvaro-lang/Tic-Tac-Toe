
from django.db import models

class Game(models.Model):

    player1 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='player2')
    winner = models.ForeignKey('Player', on_delete=models.CASCADE, related_name='winner')
    board = models.CharField(max_length=150)

    class Meta:
        db_table = 'game'