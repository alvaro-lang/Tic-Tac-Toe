from django.test import TestCase
from ..src.Play import Play

class TestCheckVictory(TestCase):

    def setUp(self):
        self.play = Play()
    
    def testCheckVictory(self):
        board = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["_", "_", "O"]
        ]
        self.assertTrue(self.play.checkVictory(board, "X"))

    def testCheckVictory2(self):
        board = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["X", "_", "O"]
        ]
        self.assertTrue(self.play.checkVictory(board, "X"))

    def testCheckVictory3(self):
        board = [
            ["O", "X", "X"],
            ["O", "O", "X"],
            ["_", "X", "O"]
        ]
        self.assertTrue(self.play.checkVictory(board, "O"))
    
    def testCheckVictory4(self):
        board = [
            ["O", "O", "X"],
            ["X", "O", "O"],
            ["_", "X", "X"]
        ]
        self.assertFalse(self.play.checkVictory(board, "O"))