import os
from .text import theme

import sys
sys.path.append('..')
import Minesweeper

sys.path.append('controllers')
from gameController import *

def show_celula(element, secret_field, show_mines=False):
  if show_mines and secret_field == Minesweeper.MINE:
    print(RED + '%4s' %(MINE) + COLOR_END, end='')
  elif element != 0:
    print(GREEN + '%4s' %(secret_field) + COLOR_END, end='')
  else:
    print(YELLOW + '%4s' %(EMPTY) + COLOR_END, end='')

def show_formatted_grid(grid, grid_state, status, r, c):
  os.system('clear')
  print('%23s\n' %('CAMPO MINADO'))

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

def coordinates_by_user():
  return [int(i) for i in input('\n       insira as coordenadas: ').split(' ')]

def show(msg):
  print('\n\n%23s\n' %msg)
  input('Aperte qualquer tecla para continuar...')

def select_menu():
  os.system('clear')

  print(theme)
  print('1 - JOGAR')
  print('2 - SAIR')

  op = input('\nsua escolha: ')
  return op
