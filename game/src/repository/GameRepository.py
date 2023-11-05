from ...models.Game import Game
from .PlayerRepository import PlayerRepository

class GameRepository():

    def insert(self, player1, player2, winner, draw):

        game = Game()

        game.player1 = PlayerRepository().getPlayerByName(player1)
        game.player2 = PlayerRepository().getPlayerByName(player2)
        game.winner = PlayerRepository().getPlayerByName(winner)
        game.draw = draw

        game.save()

        return game
