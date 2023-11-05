import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Tic_Tac_Toe.settings")
import django
django.setup()

from game.src.GameMenu import GameMenu

GameMenu().menu()