from django.test import TestCase
from ..src.Play import Play

class TestCheckBoardCompleted(TestCase):

    def setUp(self):
        self.play = Play()
    
    def testCheckBoardCompleted(self):
        boardCompleted = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.play.checkBoardCompleted(boardCompleted))

    def testCheckBoardCompleted2(self):
        boardInCompleted = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["_", "_", "O"]
        ]
        self.assertFalse(self.play.checkBoardCompleted(boardInCompleted))

        