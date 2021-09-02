from agents.Robot import Robot

# Structure to hold info about current robot task and destination
class Task():
       def __init__(self, robot: Robot, source: tuple, destination: tuple):
        self.robot = robot
        self.destination = destination
        self.source = source
