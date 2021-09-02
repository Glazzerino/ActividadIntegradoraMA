import agentpy as ap
import math
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
      self.grid.add_agents(self.robots, random=True) # Random positions
      self.robots.set_position(self.grid) # Communicate positions to each robot

      # Calculate diagonal
      self.diagonal = int(math.sqrt(math.pow(self.p.size, 2)))
      self.robots.set_diagonal(self.diagonal)
      self.br_router = {}
      # Share reference to dictionary with robots

      # Shameful O(n^2) loop
      for robot in self.robots:
         mindistance = self.diagonal
         box_target = None
         for box in self.boxes:
            if box.id in self.br_router:
               continue
            else:
               boxpos = self.grid.positions[box]
               distance = self.point_distance(robot.get_position(), boxpos)
               if distance < mindistance:
                  mindistance = distance
                  box_target = box
         # Register "task"
         self.br_router[box_target.id] = robot.id
         target_position = self.grid.positions[box_target]
         robot.set_target(target_position)

   def step(self):
      self.robots.step()

   def point_distance(self, point1, point2):
      return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))