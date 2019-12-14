from Minesweeper import Minesweeper
from Matrix import Matrix
import os

YELLOW    = '\033[93m'
GREEN     = '\033[92m'
RED       = '\033[31m'
COLOR_END = '\033[0;0m'

def show_formatted_grid(grid, r, c):

  print('%19s\n' %('CAMPO MINADO'))
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
        secret_element = grid.get_element(row, col)

        if element != 0:
          print(GREEN + '%4s' %(secret_element) + COLOR_END, end='')
        elif r == row and c == col:
          print(GREEN + '%4s' %(secret_element) + COLOR_END, end='')
          grid_state.set_element(row, col, 1)
        else:
          print(YELLOW + '%4s' %('◻') + COLOR_END, end='')

    print()


def coordinates_by_user():
  return [int(i) for i in input('\n       insira as coordenadas: ').split(' ')]


game = Minesweeper()
grid_state = Matrix(game.height, game.width)

row, column = -1, -1

while True:

  os.system('clear')
  show_formatted_grid(game.grid, row, column)
  row, column = coordinates_by_user()

