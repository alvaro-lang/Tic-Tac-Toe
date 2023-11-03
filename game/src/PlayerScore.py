from .repository.PlayerRepository import PlayerRepository
from colorama import Fore, Style

class PlayerScore():

    def showPlayersScore(self):
        players = PlayerRepository().getAllPlayers()

        print("#####################################")
        print(f"# {Fore.LIGHTGREEN_EX}PARTIDAS GANADAS DE LOS JUGADORES{Style.RESET_ALL} #")
        print("#####################################")

        print("-----------------------------")
        for player in players:
            playerName = player.name.ljust(15)
            gamesWon = str(player.gamesWon).rjust(5)
            print(f"{playerName}: {gamesWon}")
        print("-----------------------------")

        input("\nPulsa intro para volver al menú...")