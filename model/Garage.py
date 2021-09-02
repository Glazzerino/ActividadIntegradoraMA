import agentpy as ap
import math
import random
from agents.Robot import Robot


class Garage(ap.Model):
   def setup(self):
      # Create space and instantiate agents
      self.grid = ap.Grid(self, [self.p.size]*2, track_empty=True)
      self.robots = self.robots = ap.AgentList(self, self.p.robots, Robot)
      self.boxes = ap.AgentList(self, self.p["boxes"])
      # 0 for misplaced, 1 for correctly placed, 2 means robot
      self.boxes.condition = 0
      self.boxes.type = "box"
      self.robots.condition = 2
      self.grid.add_agents(self.boxes, random=True)
      self.grid.add_agents(self.robots, random=True)
      self.robots.set_location(self.grid)

      # Calculate diagonal
      self.diagonal = int(math.sqrt(math.pow(self.p.size, 2)))
      print(self.diagonal)
      self.robots.set_diagonal(self.diagonal)
      for robot in self.robots:
         neighbors = self.grid.neighbors(robot, distance=self.diagonal)
         for neighbor in neighbors:
            if neighbor.type == "box":
               neighbor.condition = 3

   def step(self):
      self.robots.step()