
from django.test import TestCase
from ...src.repository.GameRepository import GameRepository

class TestInsertGame(TestCase):

    def testInsert(self):

        game = GameRepository().insert("Invitado1", "Invitado2", None, True)
        
        self.assertEqual(1, game.id)