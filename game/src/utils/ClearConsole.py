
import platform
import os

class ClearConsole():

    def clear(self):

        # Get OS name
        name = platform.system()

        if name == "Windows":
            os.system('cls')
        else:
            os.system('clear')