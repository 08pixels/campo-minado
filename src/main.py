from views.game import *
from Minesweeper import Minesweeper

while True:
  op = selection_menu()

  if op == '1':
    game = Minesweeper()
    # an invalid position
    row, column = -1, -1
    status = Minesweeper.GAMING

    while status == Minesweeper.GAMING:
      game.make_moviment(row, column)
      status = game.get_status(row, column)
      show_formatted_grid(game, status)

      if status == Minesweeper.GAME_OVER:
        show_end_message('VOCÊ PERDEU!')
      elif status == Minesweeper.GAME_WIN:
        show_end_message('VOCÊ VENCEU!!!')
      else:
        row, column = get_coordinates()

  elif op == '2': # sair
    break

