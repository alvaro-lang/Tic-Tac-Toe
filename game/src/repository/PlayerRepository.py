from ...models.Player import Player

class PlayerRepository():

    def addVictory(self, playerSymbol):
        player = None

        if playerSymbol == "X":
            player = Player.objects.get(name = "Invitado1")

        elif playerSymbol == "O":
            player = Player.objects.get(name = "Invitado2")

        if player != None:
            player.gamesWon += 1
            player.save()

        return player

    def getAllPlayers(self):
        return Player.objects.all()
    
    def getPlayerByName(self, playerName):
        return Player.objects.get(name=playerName)