import constants as c
import pyrosim.pyrosim as pyrosim
import numpy
import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setGravity(0,0,c.gravity, physicsClient)

planeId = p.loadURDF("plane.urdf")

p.loadSDF("world.sdf")
# Robot
robotId = p.loadURDF("body.urdf")  # the robot link
pyrosim.Prepare_To_Simulate(robotId)
numberOfSteps = c.numberOfSteps
p.resetDebugVisualizerCamera(
    cameraDistance=7,
    cameraYaw=45,
    cameraPitch=-30,
    cameraTargetPosition=[0, 0, 1])  # roughly center on the robot
#pauses the program for 1/60th of a second 
frontLegSensorValues = numpy.zeros(numberOfSteps)
backLegSensorValues = numpy.zeros(numberOfSteps)

# add parameters
# Back leg parameters
backAmplitude = numpy.pi / 4
backFrequency = 10
backPhaseOffset = 0

# Front leg parameters
frontAmplitude = numpy.pi / 4
frontFrequency = 10
frontPhaseOffset = numpy.pi / 2   # <-- this breaks symmetry

backLegAngles = numpy.zeros(numberOfSteps)
frontLegAngles = numpy.zeros(numberOfSteps)

for i in range(numberOfSteps):
    backLegAngles[i] = backAmplitude * numpy.sin(
        2 * numpy.pi * backFrequency * i / numberOfSteps + backPhaseOffset
    )

    frontLegAngles[i] = frontAmplitude * numpy.sin(
        2 * numpy.pi * frontFrequency * i / numberOfSteps + frontPhaseOffset
    )



#PRINT ITERATION
for i in range(numberOfSteps):
	p.stepSimulation()
	backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
	frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
	pyrosim.Set_Motor_For_Joint(
		bodyIndex=robotId, 
		jointName=b"Torso_BackLeg",
	        controlMode=p.POSITION_CONTROL,
	        targetPosition=backLegAngles[i],
		maxForce=c.maxForce)	
	pyrosim.Set_Motor_For_Joint(
       	        bodyIndex=robotId,
       	        jointName=b"Torso_FrontLeg",
        	controlMode=p.POSITION_CONTROL,
        	targetPosition=frontLegAngles[i],
        	maxForce=c.maxForce)

	time.sleep(c.sleepTime)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegAngles.npy", backLegAngles)
numpy.save("data/frontLegAngles.npy", frontLegAngles)
numpy.save("data/targetAngles.npy", targetAngles)
exit()
p.disconnect()

