from Minesweeper import Minesweeper
from Matrix import Matrix
import os
import text

YELLOW    = '\033[93m'
GREEN     = '\033[92m'
RED       = '\033[31m'
COLOR_END = '\033[0;0m'

GAMING    = 0
GAME_WIN  = 1
GAME_OVER = 2

EMPTY = '◻'
MINE  = '💣'

def game_status(current_element):

  if current_element == Minesweeper.MINE:
    return GAME_OVER

  return GAMING

def show_celula(element, secret_field, show_mines=False):
  if element != 0:
    print(GREEN + '%4s' %(secret_field) + COLOR_END, end='')
  elif show_mines and secret_field == Minesweeper.MINE:
    print(RED + '%4s' %(MINE) + COLOR_END, end='')
  else:
    print(YELLOW + '%4s' %(EMPTY) + COLOR_END, end='')

def show_formatted_grid(grid, r, c):
  os.system('clear')
  print('%19s\n' %('CAMPO MINADO'))

  status = game_status(grid.get_element(r, c))
  # horizontal numbering
  for col in range(grid.width):
    if col == 0:
      print("%8d" %(col), end='')
    elif col != grid.width - 1:
      print("%4d" %(col), end='')
    else:
      print("%4d" %(col))


  for row in range(grid.height):
    # vertical numbering
    print('%4d' %(row), end='')

    for col in range(grid.width):
      if r == row and c == col:
        grid_state.set_element(row, col, 1)

      element = grid_state.get_element(row, col)
      secret_field = grid.get_element(row, col)

      if status == GAME_OVER or status == GAME_WIN:
        show_celula(element, secret_field, True)
      else:
        show_celula(element, secret_field, False)

    print()

  return status


def coordinates_by_user():
  return [int(i) for i in input('\n       insira as coordenadas: ').split(' ')]


def select_menu():
  print(text.theme)
  print('1 - JOGAR')
  print('2 - SAIR')

  op = input('\nsua escolha: ')
  return op



while True:
  os.system('clear')
  op = select_menu()

  if op == '1': # jogar
    game = Minesweeper()
    grid_state = Matrix(game.height, game.width)
    row, column = -1, -1

    while True:
      status = show_formatted_grid(game.grid, row, column)

      if status != GAMING:
        break

      row, column = coordinates_by_user()

  elif op == '2': # sair
    break

