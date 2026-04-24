import numpy
import os
import constants as c
import pyrosim.pyrosim as pyrosim
class SOLUTION:

    def __init__(self, myID):

        self.myID = myID
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
       
       # print("Before:", self.weights)

        self.weights = self.weights * 2 - 1

        #print("After:", self.weights)

        
    # Start SDF file
    # Step 1: Create the world
    # One cube at origin
    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[0,-3,0.5], size=[1,1,1])
# End SDF file
        pyrosim.End()
# Step 2: Create the robot
    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
    # ----------------
    # Torso (root link)
    # ----------------
        pyrosim.Send_Cube(
            name="Torso",
            pos=[0, 0, 1],     # absolute
            size=[1, 1, 1]
        )

    # ----------------
    # Back leg
    # ----------------
        pyrosim.Send_Joint(
            name="Torso_BackLeg",
            parent="Torso",
            child="BackLeg",
            type="revolute",
            position=[0,-0.5, 1.0],
            jointAxis="1 0 0"

   # absolute (bottom of torso)
        )

        pyrosim.Send_Cube(
            name="BackLeg",
            pos=[0,-0.5, 0],    # relative to joint
            size=[0.2, 1, 0.2]
        )
        pyrosim.Send_Joint(
            name="BackLeg_BackLowerLeg",
            parent="BackLeg",
            child="BackLowerLeg",
            type="revolute",
            position=[0, -1.0, 0],
            jointAxis="1 0 0"
        )
        pyrosim.Send_Cube(
            name="BackLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )
    # ----------------
    # Front leg
    # ----------------
        pyrosim.Send_Joint(
            name="Torso_FrontLeg",
            parent="Torso",
            child="FrontLeg",
            type="revolute",
            position=[0, 0.5, 1.0],
            jointAxis="1 0 0"  # absolute (front face of torso)
        )

        pyrosim.Send_Cube(
            name="FrontLeg",
            pos=[0, 0.5, 0],     # relative to joint
            size=[0.2, 1, 0.2]
        )
    
        pyrosim.Send_Joint(
            name="FrontLeg_FrontLowerLeg",
            parent="FrontLeg",
            child="FrontLowerLeg",
            type="revolute",
            position=[0, 1.0, 0],
            jointAxis="1 0 0"
        )
        pyrosim.Send_Cube(
            name="FrontLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )
        pyrosim.Send_Joint(
            name="Torso_LeftLeg",
            parent="Torso",
            child="LeftLeg",
            type="revolute",
            position=[-0.5, 0, 1],
            jointAxis="0 1 0"
        )  
        pyrosim.Send_Cube(
            name="LeftLeg",
            pos=[-0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="LeftLeg_LeftLowerLeg",
            parent="LeftLeg",
            child="LeftLowerLeg",
            type="revolute",
            position=[-1.0, 0, 0],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="LeftLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )
# middle left leg
        pyrosim.Send_Joint(
            name="Torso_MiddleLeftLeg",
            parent="Torso",
            child="MiddleLeftLeg",
            type="revolute",
            position=[-0.5, -0.25, 1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="MiddleLeftLeg",
            pos=[-0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )

        pyrosim.Send_Joint(
            name="MiddleLeftLeg_MiddleLeftLowerLeg",
            parent="MiddleLeftLeg",
            child="MiddleLeftLowerLeg",
            type="revolute",
            position=[-1.0, 0, 0],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="MiddleLeftLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )

# torso right leg
        pyrosim.Send_Joint(
            name="Torso_RightLeg",
            parent="Torso",
            child="RightLeg",
            type="revolute",
            position=[0.5, 0, 1],
            jointAxis="0 1 0"
        )
        pyrosim.Send_Cube(
            name="RightLeg",
            pos=[0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )
        pyrosim.Send_Joint(
            name="RightLeg_RightLowerLeg",
            parent="RightLeg",
            child="RightLowerLeg",
            type="revolute",
            position=[1.0, 0, 0],
            jointAxis="0 1 0"
        )
        pyrosim.Send_Cube(
            name="RightLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )
#torso middle right leg
        pyrosim.Send_Joint(
            name="Torso_MiddleRightLeg",
            parent="Torso",
            child="MiddleRightLeg",
            type="revolute",
            position=[0.5, 0.25, 1],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="MiddleRightLeg",
            pos=[0.5, 0, 0],
            size=[1, 0.2, 0.2]
        )
        pyrosim.Send_Joint(
            name="MiddleRightLeg_MiddleRightLowerLeg",
            parent="MiddleRightLeg",
            child="MiddleRightLowerLeg",
            type="revolute",
            position=[1.0, 0, 0],
            jointAxis="0 1 0"
        )

        pyrosim.Send_Cube(
            name="MiddleRightLowerLeg",
            pos=[0, 0, -0.5],
            size=[0.2, 0.2, 1]
        )

        pyrosim.End()
# Step 2: Create the robot
    def Generate_Brain(self):
        import time
        import os
        pyrosim.Start_NeuralNetwork(f"brain{self.myID}.nndf")
        pyrosim.Send_Sensor_Neuron(
	    name=0,
	    linkName="Torso"
        )
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=9, linkName="MiddleLeftLeg")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="MiddleRightLeg")
        pyrosim.Send_Sensor_Neuron(name=11, linkName="MiddleLeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name=12, linkName="MiddleRightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Torso_RightLeg")
        pyrosim.Send_Motor_Neuron(name=17, jointName="FrontLeg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron(name=18, jointName="BackLeg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron(name=19, jointName="LeftLeg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=20, jointName="RightLeg_RightLowerLeg")
        pyrosim.Send_Motor_Neuron(name=21, jointName="Torso_MiddleLeftLeg")
        pyrosim.Send_Motor_Neuron(name=22, jointName="Torso_MiddleRightLeg")
        pyrosim.Send_Motor_Neuron(name=23, jointName="MiddleLeftLeg_MiddleLeftLowerLeg")
        pyrosim.Send_Motor_Neuron(name=24, jointName="MiddleRightLeg_MiddleRightLowerLeg")

        for i in range(c.numSensorNeurons):      # 0,1,2
            for j in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=i,
                    targetNeuronName=j + c.numSensorNeurons,
                    weight=self.weights[i][j]
                )    
        pyrosim.End()
        brainFileName = f"brain{self.myID}.nndf"
        while not os.path.exists(brainFileName):
             time.sleep(0.01)
    def Start_Simulation(self, mode):
        self.Create_World()  
        self.Generate_Body() 
        self.Generate_Brain()
        import os
        os.system(f"python simulate.py {mode} {self.myID} &")
    def Wait_For_Simulation_To_End(self):
        import time
        import os
        fitnessFileName = f"fitness{self.myID}.txt"
        while True:
            if os.path.exists(fitnessFileName):
                with open(fitnessFileName, "r") as f:
                    content = f.read()
                    if content != "":
                        self.fitness = float(content)
                        break
            time.sleep(0.01)        
        print("Fitness:", self.fitness)
        
        os.system(f"rm fitness{self.myID}.txt")
  
 # def Evaluate(self, mode):
    #    self.Create_World()   
     #   self.Generate_Body()
      #  self.Generate_Brain()
       # import os
        #os.system(f"python simulate.py {mode} {self.myID} &")
       # f = open(f"fitness{self.myID}.txt", "r")
       # self.fitness = float(f.read())
       # f.close()

       # print("Fitness:", self.fitness)
    def Copy(self):
    
        newSolution = SOLUTION(self.myID)

        newSolution.weights = self.weights.copy()

        return newSolution
    def Mutate(self):

        i = numpy.random.randint(0,c.numSensorNeurons)
        j = numpy.random.randint(0,c.numMotorNeurons)

        self.weights[i][j] = numpy.random.rand() * 2 - 1
    def Set_ID(self, myID):
        self.myID = myID
