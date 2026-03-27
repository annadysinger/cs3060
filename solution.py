import numpy
import os
import constants as c
import pyrosim.pyrosim as pyrosim
class SOLUTION:

    def __init__(self, myID):
        print("Creating solution with ID:", myID)
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
            position=[1.0, 0, 1.0]

   # absolute (bottom of torso)
        )

        pyrosim.Send_Cube(
            name="BackLeg",
            pos=[-0.5, 0, -0.5],    # relative to joint
            size=[1, 1, 1]
        )

    # ----------------
    # Front leg
    # ----------------
        pyrosim.Send_Joint(
            name="Torso_FrontLeg",
            parent="Torso",
            child="FrontLeg",
            type="revolute",
            position=[2.0, 0, 1.0]  # absolute (front face of torso)
        )

        pyrosim.Send_Cube(
            name="FrontLeg",
            pos=[0.5, 0, -0.5],     # relative to joint
            size=[1, 1, 1]
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

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    
        for i in range(c.numSensorNeurons):      # 0,1,2
            for j in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(
                    sourceNeuronName=i,
                    targetNeuronName=j + 3,
                    weight=self.weights[i][j]
                )    
        pyrosim.End()
        brainFileName = f"brain{self.myID}.nndf"
        while not os.path.exists(brainFileName):
             time.sleep(0.01)
        exit()
    def Start_Simulation(self, mode):
        print("start simulation with ID:", self.myID, "mode:", mode)
        self.Create_World()  
        self.Generate_Body() 
        self.Generate_Brain()
        import os
        import sys
        import subprocess
  #      subprocess.run(
 #           [sys.executable, "simulate.py", mode, str(self.myID)]
#        )
        os.system(f"{sys.executable} simulate.py {mode} {self.myID} &")
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
