import random
from Matrix import Matrix

class Minesweeper:
  RATE = 0.16
  MINE = -1
  EMPTY= 0

  def __init__(self):
    self.width = 6
    self.height = 6
    self.amount_of_mines = int((self.width * self.height) * Minesweeper.RATE)
    self.mines_position = self.mines_generator()
    self.amount_of_free_squares = (self.width * self.height) - self.amount_of_mines

    self.grid = Matrix(self.height, self.width)
    self.grid = self.mines_populate(self.grid)
    self.grid = self.count_mines_around(self.grid)

  def update_free_squares(self):
    self.amount_of_free_squares -= 1

  def mines_populate(self, grid):
    for (i, j) in self.mines_position:
      grid.set_element(i, j, Minesweeper.MINE)

    return grid

  def mines_generator(self):
    mines_position = set()

    # adding (i,j)-coordinates to the set
    # set does not allow equal elements
    while len(mines_position) != self.amount_of_mines:
      i = random.randint(0, self.height - 1)
      j = random.randint(0, self.width - 1)

      mines_position.add((i,j))

    return mines_position

  def check_mine(self, grid, row, col):
    if row < 0 or row >= self.height:
      return False
    if col < 0 or col >= self.width:
      return False
    if grid.get_element(row, col) != Minesweeper.MINE:
      return False

    return True

  def count_mines_around(self, grid):
    # neighbourhood
    mov_row = [0,1, 0,-1, 1,-1, 1,-1]
    mov_col = [1,0,-1, 0,-1, 1, 1,-1]

    for row in range(self.height):
      for col in range(self.width):
          element = grid.get_element(row, col)

          if element == Minesweeper.MINE:
            continue

          for step in range(8):
            i = row + mov_row[step]
            j = col + mov_col[step]

            if self.check_mine(grid, i, j):
              grid.set_element(row, col, 1 + grid.get_element(row, col))

    return grid

