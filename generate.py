import pyrosim.pyrosim as pyrosim

# Start SDF file
# Step 1: Create the world
# One cube at origin
def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[0,-3,0.5], size=[1,1,1])
# End SDF file
    pyrosim.End()
# Step 2: Create the robot
def Create_Robot():
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
        position=[1.0, 0, 1.0]   # absolute (bottom of torso)
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
        position=[2.0, 0, 1.0]   # absolute (front face of torso)
    )

    pyrosim.Send_Cube(
        name="FrontLeg",
        pos=[0.5, 0, -0.5],     # relative to joint
        size=[1, 1, 1]
    )
    
    pyrosim.End()
Create_World()
Create_Robot()
