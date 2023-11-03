from django.test import TestCase
from ...src.repository.PlayerRepository import PlayerRepository

class TestAddVictory(TestCase):

    def testAddVictory(self):
        player = PlayerRepository().addVictory('X')

        self.assertEqual(1, player.gamesWon)