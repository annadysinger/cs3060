import pybullet as p
import pybullet_data
import time
import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:

    def __init__(self):

        self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setGravity(0, 0, c.gravity)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):

        for t in range(c.numberOfSteps):
            p.stepSimulation()
           # self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(c.sleepTime)
        self.robot.Save_Sensor_Values()
    def __del__(self):
        p.disconnect()
