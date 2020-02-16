import sys
sys.path.append('..')
from Minesweeper import Minesweeper
from Matrix import Matrix

GAMING    = 0
GAME_WIN  = 1
GAME_OVER = 2

EMPTY = '◻'
MINE  = '💣'

YELLOW    = '\033[93m'
GREEN     = '\033[92m'
RED       = '\033[31m'
COLOR_END = '\033[0;0m'

def game_status(current_element):

  if current_element == Minesweeper.MINE:
    return GAME_OVER

  return GAMING

