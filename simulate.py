import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,-9.8, physicsClient)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
# Robot
robotId = p.loadURDF("body.urdf")  # the robot link
pyrosim.Prepare_To_Simulate(robotId)

p.resetDebugVisualizerCamera(
    cameraDistance=7,
    cameraYaw=45,
    cameraPitch=-30,
    cameraTargetPosition=[0, 0, 1])  # roughly center on the robot
#pauses the program for 1/60th of a second 

backLegSensorValues = numpy.zeros(1000)
print(backLegSensorValues)
exit()

#PRINT ITERATION
for i in range(1000):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	time.sleep(1/60)

p.disconnect()

