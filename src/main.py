import os

from views.game import *
from controllers.gameController import *
from Minesweeper import Minesweeper

while True:
  op = select_menu()

  if op == '1':
    game = Minesweeper()
    grid_state = Matrix(game.height, game.width)
    row, column = -1, -1

    status = GAMING

    while status == GAMING:
      status = game_status(game, grid_state, game.grid.get_element(row,column))
      show_formatted_grid(game.grid, grid_state, status, row, column)

      if status == GAME_OVER:
        show('VOCÊ PERDEU!')
      elif status == GAME_WIN:
        show('VOCÊ VENCEU!!!')
      else:
        row, column = coordinates_by_user()

  elif op == '2': # sair
    break

