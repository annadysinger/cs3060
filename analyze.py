import numpy
import matplotlib.pyplot as plt

backLegAngles = numpy.load("data/backLegAngles.npy")
frontLegAngles = numpy.load("data/frontLegAngles.npy")

plt.plot(backLegAngles, label="Back Leg", linewidth=3)
plt.plot(frontLegAngles, label="Front Leg")

plt.legend()
plt.show()
