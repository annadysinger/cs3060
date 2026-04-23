import numpy
import matplotlib.pyplot as plt

quad = numpy.load("quadrupedFitness.npy")
hexa = numpy.load("hexapodFitness.npy")

quad_avg = numpy.mean(quad, axis=0)
hexa_avg = numpy.mean(hexa, axis=0)

plt.plot(quad_avg, label="Quadruped")
plt.plot(hexa_avg, label="Hexapod")

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.legend()

plt.show()
