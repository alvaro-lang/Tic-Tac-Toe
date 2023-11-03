from django.test import TestCase
from ...src.repository.PlayerRepository import PlayerRepository

class TestGetPlayerByName(TestCase):

    def testGetPlayerByName(self):

        player = PlayerRepository().getPlayerByName("Invitado1")
        
        self.assertEqual(1, player.id)