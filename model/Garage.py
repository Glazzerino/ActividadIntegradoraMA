import agentpy as ap
import math
from agents.Robot import Robot

class Garage(ap.Model):

   def assign_target(self, robot: Robot):
      if not robot.is_fetching():
         robot.set_target(self.goal)
      mindistance = self.diagonal
      box_target = None
      boxpos_target = None
      for box in self.boxes:
         if box.id in self.br_router or box.condition == 1:
            continue
         boxpos = self.grid.positions[box]
         distance = self.point_distance(boxpos, robot.get_position())
         if distance < mindistance:
            mindistance = distance
            box_target = box
            boxpos_target = boxpos
      if box_target != None:
         robot.set_target(boxpos_target)
         self.br_router[box_target.id] = robot
         
   def point_distance(self, point1, point2):
      return math.sqrt(math.pow(point1[0] - point2[0], 2) + math.pow(point1[1] - point2[1], 2))

   def setup(self):
      # Create space and instantiate agents
      self.grid = ap.Grid(self, [self.p.size]*2, track_empty=True)
      self.robots = self.robots = ap.AgentList(self, self.p.robots, Robot)
      self.boxes = ap.AgentList(self, self.p["boxes"])
      # 0 for misplaced, 1 for picked up, 2 means robot
      self.boxes.condition = 0
      self.boxes.type = "box"
      self.robots.condition = 2
      self.grid.add_agents(self.boxes, random=True)
      self.grid.add_agents(self.robots, random=True) # Random positions
      self.robots.set_position(self.grid) # Communicate positions to each robot
      self.goal = [0, 0]
      self.goal_counter = {}
      self.goal_counter[str(self.goal)] = 0
      # Calculate diagonal
      self.diagonal = int(math.sqrt(math.pow(self.p.size, 2)))
      self.robots.set_diagonal(self.diagonal)
      self.br_router = {}
      # Share reference to dictionary with robots

      # Shameful O(n^2) loop
      for robot in self.robots:
         self.assign_target(robot)
   def step(self):
      for robot in self.robots:
         robot.step()
         if (robot.is_fetching()):
            distance = self.point_distance(robot.get_position(), robot.get_target_pos())
            if abs(distance) <= 1:
               box = self.grid.agents[robot.get_target_pos()].to_list()
               for agent in box:
                  if agent.type == "box":
                     box = agent
               box.condition = 1
               robot.counter_add()
               self.assign_target(robot)
         else:
            robot_goal_distance = abs(self.point_distance(robot.get_position(), self.goal))
            if (robot_goal_distance <= 1):
               self.goal_counter[str(self.goal)] += robot.get_counter()
               if self.goal_counter[str(self.goal)] == 5:
                  self.goal = self.goal[::-1]
                  self.goal_counter[str(self.goal)] = 0

            
# pos = self.positions[agent]  # Get position
#             self.grid.agents[pos].remove(agent)  # Remove agent from grid
#             del self.positions[agent]  # Remove agent from position dict
#             if self._track_empty:
#                 self.empty.append(pos)  # Add position to free spots

           

