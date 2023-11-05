from ...models.Game import Game
from .PlayerRepository import PlayerRepository
import json

class GameRepository():

    def insert(self, player1, player2, winner, draw, board):

        game = Game()

        game.player1 = PlayerRepository().getPlayerByName(player1)
        game.player2 = PlayerRepository().getPlayerByName(player2)
        game.winner = PlayerRepository().getPlayerByName(winner)
        game.draw = draw
        game.board = json.dumps(board)

        game.save()

        return game
