import agentpy as ap
from enum import Enum

class Direction(Enum):
   LEFT = 0
   RIGHT = 1
   UP = 2
   DOWN = 3

class Robot(ap.Agent):

   def setup(self):
      self.box_count = 0
      self.fetching = False

   def set_location(self, grid: ap.Grid):
      self.grid = grid
      self.position = grid.positions[self]
   
   def get_movement_delta(self, direction: Direction):
      delta = (0, 0)
      if direction == Direction.UP:
         delta = (-1, 0)
      elif direction == Direction.DOWN:
         delta = (1, 0)
      elif direction == Direction.LEFT:
         delta = (0, -1)
      elif direction == Direction.RIGHT:
         delta = (0, 1)
      else:
         print("ERROR; Invalid direction parameter")
      return delta

   def step(self):
      # if not self.fetching:
      #    boxes = []
      #    neighbors = self.grid.neighbors(self, distance=self.diagonal)
      #    fetchbox = None
      #    mindistance = self.diagonal
      #    for n in neighbors:
      #       if n.type == "box":
      #          boxpos = self.grid.positions[n]

      #          # Print the box position
      #          print("Box found at: " + str(boxpos))
      delta = self.get_movement_delta(Direction.UP)
      self.grid.move_by(self, delta)

   def set_diagonal(self, diagonal):
      self.diagonal = diagonal
