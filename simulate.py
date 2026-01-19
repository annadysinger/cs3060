import pybullet as p
import time

physicsClient = p.connect(p.GUI)
#pauses the program for 1/60th of a second 
#PRINT ITERATION
for i in range(1000):
	p.stepSimulation()
	time.sleep(1/60)
	print(i)

p.disconnect()

