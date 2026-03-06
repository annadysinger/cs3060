import pyrosim.pyrosim as pyrosim
import numpy
import constants as c


class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.numberOfSteps)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    def Save_Values(self):

        numpy.save(f"data/{self.linkName}_SensorValues.npy", self.values)
