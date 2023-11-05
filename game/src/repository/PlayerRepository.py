from ...models.Player import Player

class PlayerRepository():

    def addVictory(self, playerSymbol):
        player = None

        if playerSymbol == "X":
            player = self.getPlayerByName("Invitado1")

        elif playerSymbol == "O":
            player = self.getPlayerByName("Invitado2")

        if player != None:
            player.gamesWon += 1
            player.save()

        return player

    def getAllPlayers(self):
        return Player.objects.all()
    
    def getPlayerByName(self, playerName):
        if (not playerName == None):
            return Player.objects.get(name=playerName)
        
        return None