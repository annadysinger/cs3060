import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import constants as c


class MOTOR:
    def __init__(self, jointName):

        self.jointName = jointName


    def Set_Value(self, robotId, desiredAngle):

        jointName = self.jointName

        # Fix for Mac string/bytes issue
        if type(jointName) is str:
            jointName = jointName.encode("utf-8")

        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=desiredAngle,
            maxForce=c.maxForce
        )          
