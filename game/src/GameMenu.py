from .Play import Play
from colorama import Fore, Style
from .PlayerScore import PlayerScore
from .utils.ClearConsole import ClearConsole

class GameMenu():

    def menu(self):

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

            selectedOption = int(input("\nSelecciona una opción: "))
            
            # Use ClearConsole to dont have repetitive logs in your console.
            ClearConsole().clear()
            
            if selectedOption == 1:
                Play().playGame()
            elif selectedOption == 2:
                print()
            elif selectedOption == 3:
                PlayerScore().showPlayersScore()
            elif selectedOption == 4:
                break
            else:
                print(f"\n{Fore.RED}SELECCIONA UN VALOR DE LAS OPCIONES INDICADAS.{Style.RESET_ALL}")

