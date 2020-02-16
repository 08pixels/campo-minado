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
      status = show_formatted_grid(game.grid, grid_state, row, column)

      if status == GAME_OVER:
        print('GAME OVER')
        print('Aperte qualquer tecla para continuar')
        input()
        break
      if status == GAME_WIN:
        print('YOU WON')
        print('Aperte qualquer tecla para continuar')
        input()
        break

      row, column = coordinates_by_user()

  elif op == '2': # sair
    break

