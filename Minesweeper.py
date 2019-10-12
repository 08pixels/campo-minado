import random

class Minesweeper:
  RATE = 0.16
  MINE = -1
  EMPTY= 0

  def __init__(self):
    self.width = 16
    self.height = 16
    self.amount_of_mines = int((self.width * self.height) * Minesweeper.RATE)
    self.mines_position = self.mines_generator()
    self.grid = self.create_grid()

  def empty_row(self):
    return [Minesweeper.EMPTY for i in range(self.width)]
  
  def create_grid(self):
    grid = [self.empty_row() for i in range(self.height)]

    # adding mines in the grid
    for (i, j) in self.mines_position:
      grid[i][j] = Minesweeper.MINE

    # counting mines around the cells
    grid = self.count_mines_around(grid)
    
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
    if grid[row][col] != Minesweeper.MINE:
      return False

    return True


  def count_mines_around(self, grid):
    # possible moviments
    mov_row = [0,1, 0,-1, 1,-1, 1,-1]
    mov_col = [1,0,-1, 0,-1, 1, 1,-1]

    for row in range(self.height):
      for col in range(self.width):
          if grid[row][col] == Minesweeper.MINE:
            continue

          for step in range(8):
            i = row + mov_row[step]
            j = col + mov_col[step]

            if self.check_mine(grid, i, j):
              grid[row][col] += 1

    return grid
  
