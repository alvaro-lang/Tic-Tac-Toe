from .Play import Play
from colorama import Fore, Style

class GameMenu():

    def menu(self):
        play = Play()

        while True:
            print("\n############################")
            print(f"# {Fore.YELLOW}BIENVENIDO A TIC-TAC-TOE{Style.RESET_ALL} #")
            print("############################\n")

            print("1 - Jugar una partida.")
            print("2 - Ver partidas jugadas.")
            print("3 - Iniciar sesión.")
            print("4 - Registrarse.")
            print("5 - Salir.")

            selectedOption = int(input("\nSelecciona una opción: "))

            if selectedOption == 1:
                play.playGame()
            elif selectedOption == 2:
                print()
            elif selectedOption == 3:
                print()
            elif selectedOption == 4:
                print()
            elif selectedOption == 5:
                break
            else:
                print(f"\n{Fore.RED}SELECCIONA UN VALOR DE LAS OPCIONES INDICADAS.{Style.RESET_ALL}")

