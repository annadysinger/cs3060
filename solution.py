import numpy
import os
import pyrosim.pyrosim as pyrosim
class SOLUTION:

    def __init__(self):
        self.weights = numpy.random.rand(3,2)
       
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
            pos=[1.5, 0, 1.5],     # absolute
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
        pyrosim.Start_NeuralNetwork("brain.nndf")

        pyrosim.Send_Sensor_Neuron(
	    name=0,
	    linkName="Torso"
        )
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    
        for i in range(3):      # 0,1,2
            for j in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName=i,
                    targetNeuronName=j + 3,
                    weight=self.weights[i][j]
                )    
        pyrosim.End()

    def Evaluate(self, mode):
        self.Create_World()   
        self.Generate_Body()
        self.Generate_Brain()
        import os
        os.system("python simulate.py {mode}")
        f = open("fitness.txt", "r")
        self.fitness = float(f.read())
        f.close()

        print("Fitness:", self.fitness)
    def Copy(self):
    
        newSolution = SOLUTION()

        newSolution.weights = self.weights.copy()

        return newSolution
    def Mutate(self):

        i = numpy.random.randint(0,3)
        j = numpy.random.randint(0,2)

        self.weights[i][j] = numpy.random.rand() * 2 - 1
