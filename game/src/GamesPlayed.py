from .repository.GameRepository import GameRepository
from colorama import Fore, Style
import ast
from .Play import Play 

class GamesPlayed():

    def printGamesPlayed(self):

        games = GameRepository().getAllGames()

        print("####################")
        print(f"# {Fore.LIGHTGREEN_EX}PARTIDAS JUGADAS{Style.RESET_ALL} #")
        print("####################\n")

        print(f"{'Tablero'.ljust(15)} {'Jugador 1'.ljust(15)} {'Jugador 2'.ljust(15)} {'Ganador'.ljust(15)} {'Empate'.ljust(15)}")
        print("##################################################################################\n")

        for game in games:
            player1 = str(game.player1.name).ljust(15)
            player2 = str(game.player2.name).ljust(15)
            if game.winner:
                winner = str(game.winner.name).ljust(15)
            else:
                winner = "Sin ganador".ljust(15)
            if game.draw:
                draw = "SI"
            else:
                draw = "NO"
            draw = draw.ljust(15)
            board = ast.literal_eval(game.board)
            board_str = ""
            lineCount = 0
            for row in board:
                boardRow = ""
                count = 0
                for symbol in row:
                    if count == 0 or count == 2:
                        boardRow += "| " + symbol + " |"
                    else:
                        boardRow += " " + symbol + " "
                    count += 1
                lineCount = lineCount + 1
                if lineCount == 3:
                    board_str += boardRow
                else:
                    board_str += boardRow + "\n" + "-------------" + "\n"


            print(f"{board_str}   {player1} {player2} {winner} {draw}")
            print("----------------------------------------------------------------------------------\n")
        
        input("\nPulsa intro para volver al menú...")