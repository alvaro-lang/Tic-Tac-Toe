from .Play import Play
from colorama import Fore, Style
from .PlayerScore import PlayerScore
from .utils.ClearConsole import ClearConsole
from .GamesPlayed import GamesPlayed

class GameMenu():

    def menu(self):
        error = False
        
        while True:

            # Use ClearConsole to dont have repetitive logs in your console.
            ClearConsole().clear()

            print("\n############################")
            print(f"# {Fore.YELLOW}BIENVENIDO A TIC-TAC-TOE{Style.RESET_ALL} #")
            print("############################\n")

            print("1 - Jugar una partida.")
            print("2 - Ver partidas jugadas.")
            print("3 - Ver puntuacion de los jugadores.")
            print("4 - Salir.")

            if error:
                print(f"\n{Fore.RED}SELECCIONA UN VALOR DE LAS OPCIONES INDICADAS.{Style.RESET_ALL}")
                error = False

            selectedOption = input("\nSelecciona una opción: ")

            if selectedOption.isdigit():
                selectedOption = int(selectedOption)
            
            # Use ClearConsole to dont have repetitive logs in your console.
            ClearConsole().clear()
            
            if selectedOption == 1:
                Play().playGame()
            elif selectedOption == 2:
                GamesPlayed().printGamesPlayed()
            elif selectedOption == 3:
                PlayerScore().showPlayersScore()
            elif selectedOption == 4:
                break
            else:
                error = True

