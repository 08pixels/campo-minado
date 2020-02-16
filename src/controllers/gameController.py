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

def input_validation(game, grid_state, row,col):

  if row < 0 or col < 0:
    return False
  if row >= game.height or col >= game.width:
    return False
  
  return grid_state[row][col] == Matrix.EMPTY


def game_status(grid, grid_state, current_element):

  if current_element == Minesweeper.MINE:
    return GAME_OVER

  if not grid.amount_of_free_squares:
    return GAME_WIN

  grid.update_free_squares()


  return GAMING

