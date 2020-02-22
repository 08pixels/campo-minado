import os
from .text import theme

import sys
sys.path.append('..')
from Minesweeper import Minesweeper

EMPTY = '◻'
MINE  = '💣'

YELLOW    = '\033[93m'
GREEN     = '\033[92m'
RED       = '\033[31m'
COLOR_END = '\033[0;0m'

def show_celula(element, secret_field, show_mines=False):
  if show_mines and secret_field == Minesweeper.MINE:
    print(RED + '%4s' %(MINE) + COLOR_END, end='')
  elif element != 0:
    print(GREEN + '%4s' %(secret_field) + COLOR_END, end='')
  else:
    print(YELLOW + '%4s' %(EMPTY) + COLOR_END, end='')

def show_formatted_grid(game, status):
  os.system('clear')

  print('%23s' %'CAMPO MINADO')
  print('%29s\n' %('QUANTIDADE DE MINAS: %d' %(game.amount_of_mines)))

  grid = game.grid
  grid_state = game.grid_state

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
      element = grid_state.get_element(row, col)
      secret_field = grid.get_element(row, col)

      if status == Minesweeper.GAME_OVER or status == Minesweeper.GAME_WIN:
        show_celula(element, secret_field, True)
      else:
        show_celula(element, secret_field, False)

    print()

def get_coordinates():

  try:
    coordinate = [int(i) for i in input('\n       insira as coordenadas: ').split()]
  except:
    return [-1, -1]

  return coordinate if (len(coordinate) == 2) else [-1, -1]

def show_end_message(msg):
  print('\n\n%23s\n' %(msg))
  input('Aperte qualquer tecla para continuar...')

def selection_menu():
  os.system('clear')

  print(theme)
  print('1 - JOGAR')
  print('2 - SAIR')

  op = input('\nsua escolha: ')
  return op
