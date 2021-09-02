import agentpy as ap
from enum import Enum

class Direction(Enum):
   LEFT = 0
   RIGHT = 1
   UP = 2
   DOWN = 3
   UPLEFT = 4
   UPRIGHT = 5
   DOWNLEFT = 6
   DOWNRIGHT = 7

class Robot(ap.Agent):

   def setup(self):
      self.box_count = 0
      self.fetching = False
      self.target = (0, 0)

   def set_position(self, grid):
      self.grid = grid
      self.position = grid.positions[self]
   def get_position(self):
      return self.position
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
      elif direction == Direction.UPLEFT:
         delta = (-1, -1)
      elif direction == Direction.UPRIGHT:
         delta = (-1, 1)
      elif direction == Direction.DOWNLEFT:
         delta = (1, -1)
      elif direction == Direction.DOWNRIGHT:
         delta = (1, 1)
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
      delta = self.get_movement_delta(Direction.DOWNRIGHT)
      self.grid.move_by(self, delta)

   def set_diagonal(self, diagonal):
      self.diagonal = diagonal
   
   def set_target(self, target: tuple):
      self.target = target
      self.fetching = True
      print("Robot got target at " + str(self.target))
