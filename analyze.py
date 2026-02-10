import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

plt.plot(frontLegSensorValues, label="FrontLeg")
plt.plot(backLegSensorValues, label="BackLeg", linewidth=3)
plt.legend()
plt.show()

