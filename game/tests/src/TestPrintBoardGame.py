from django.test import TestCase
from io import StringIO
from unittest.mock import patch
from ...src.Play import Play

class TestPrintBoardGame(TestCase):

    def setUp(self):
        self.play = Play()
    
    def testPrintBoardGame(self):
        board = [
            ["X", "X", "X"],
            ["O", "O", "X"],
            ["_", "_", "O"]
        ]
        expectedOutput = "\n-------------\n| X | X | X |\n-------------\n| O | O | X |\n-------------\n| _ | _ | O |\n-------------\n"

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.play.printBoardGame(board)
            self.assertEqual(expectedOutput, mock_stdout.getvalue())