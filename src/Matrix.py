
class Matrix:
  EMPTY = 0

  def __init__(self, height, width):
    self.height = height
    self.width = width
    self.grid = self.create_grid()


  def create_grid(self):
    empty_row = [Matrix.EMPTY for i in range(self.width)]
    grid = [empty_row.copy() for i in range(self.height)]

    return grid

  def get_element(self, pos_i, pos_j):
    return self.grid[pos_i][pos_j]

  def set_element(self, pos_i, pos_j, element):
    self.grid[pos_i][pos_j] = element

