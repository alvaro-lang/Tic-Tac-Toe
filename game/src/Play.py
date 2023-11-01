from colorama import Fore, Style

class Play():
    
    def printBoardGame(self, board):
    
        print("\n-------------")
        for row in board:
            boardRow = ""
            count = 0
            for symbol in row:
                if count == 0 or count == 2:
                    boardRow += "| " + symbol + " |"
                else:
                    boardRow += " " + symbol + " "
                count += 1

            print(boardRow)
            print("-------------")

    def checkVictory(self, board, currentPlayer):

        # Check victory in columns or rows
        for i in range(3):
            if all(board[i][j] == currentPlayer for j in range(3)) or \
            all(board[j][i] == currentPlayer for j in range(3)):
                return True

        # Check victory in diagonal
        if all(board[i][i] == currentPlayer for i in range(3))or \
        all(board[i][2 - i] == currentPlayer for i in range(3)):
            return True

        return False

    # Check if board is completed
    def checkBoardCompleted(self, board):

        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    return False
                
        return True

    def playGame(self):
        board = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]

        player1 = f"{Fore.LIGHTBLUE_EX}X{Style.RESET_ALL}"
        player2 = f"{Fore.YELLOW}O{Style.RESET_ALL}"

        currentPlayer = player1

        while True:
            print("\n########################")
            print(f"| Turno del jugador {currentPlayer}. |")
            print("########################")

            self.printBoardGame(board)

            # Game inputs
            row = int(input("Elige una fila (0, 1, 2): "))
            column = int(input("Elige una columna (0, 1, 2): "))

            if (row >= 0 and row <=2) and (column >=0 and column <=2):
                if board[row][column] == "_":
                    board[row][column] = currentPlayer
                    
                    if self.checkVictory(board, currentPlayer):
                        break
                    if self.checkBoardCompleted(board):
                        print(f"{Fore.GREEN}EMPATE. EL TABLERO HA SIDO TOTALMENTE COMPLETADO{Style.RESET_ALL}")

                    # Change player turn
                    if currentPlayer == player1:
                        currentPlayer = player2
                    else:
                        currentPlayer = player1
                else:
                    print(f"{Fore.RED}ERROR. CASILLA ACTUALMENTE OCUPADA.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}ERROR. LOS VALORES DEBEN ESTAR COMPRENDIDOS ENTRE 0 Y 2 COMO SE INDICA.{Style.RESET_ALL}")

        self.printBoardGame(board)
        print(f"{Fore.GREEN}¡VICTORIA PARA EL JUGADOR {currentPlayer}!{Style.RESET_ALL}")
