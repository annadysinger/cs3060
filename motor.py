import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import constants as c


class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName

        # Motor parameters
        self.amplitude = c.amplitude
        self.phaseOffset = c.phaseOffset

        # Make one motor oscillate at half frequency
        if b"BackLeg" in jointName:
            self.frequency = c.frequency
        else:
            self.frequency = c.frequency / 2

        # Precompute motor values
        self.motorValues = numpy.zeros(c.numberOfSteps)

        for t in range(c.numberOfSteps):
            self.motorValues[t] = self.amplitude * numpy.sin(
                self.frequency * 2 * numpy.pi * t / c.numberOfSteps
                + self.phaseOffset
            )

    def Set_Value(self, robotId, t):
        jointName = self.jointName

    # FIX FOR MAC STRING/BYTES ISSUE
        if type(jointName) is str:
            jointName = jointName.encode("utf-8")

        jointIndex = pyrosim.jointNamesToIndices[jointName]
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=c.maxForce
        )
