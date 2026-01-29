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
    
# Parent link: Torso
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5], size=[1,1,1])

    # One cube as the robot's torso
    # Joint connecting Torso to Leg
    pyrosim.Send_Joint(
        name="Link0_Link1",
        parent="Link0",
        child="Link1",
        type="revolute",
        position=[0,0,1.0]   # top of Torso / bottom of Leg
    )

    # Child link: Leg
    pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5], size=[1,1,1])
    
    # second joint
    pyrosim.Send_Joint(
        name="Link1_Link2",
        parent="Link1",
        child="Link2",
        type="revolute",
        position=[0, 0, 1.0]
    )
 

    # Link2 (relative to Link1_Link2)
    pyrosim.Send_Cube(
        name="Link2",
        pos=[0, 0, 0.5],
        size=[1, 1, 1]
    )


    # Link2 -> Link4 (sideways)
    pyrosim.Send_Joint(
        name="Link2_Link4",
        parent="Link2",
        child="Link4",
        type="revolute",
        position=[0, 0.5, 0.5]
    )

    pyrosim.Send_Cube(
        name="Link4",
        pos=[0, 0.5, 0],
        size=[1, 1, 1]
    )

    # Link4 -> Link5 (sideways)
    pyrosim.Send_Joint(
        name="Link4_Link5",
        parent="Link4",
        child="Link5",
        type="revolute",
        position=[0, 1.0, 0]
    )

    pyrosim.Send_Cube(
        name="Link5",
        pos=[0, 0.5, 0],
        size=[1, 1, 1]
    )
	
    # Joint 5 -> 6 (DOWN)
    pyrosim.Send_Joint(
        name="Link5_Link6",
        parent="Link5",
        child="Link6",
        type="revolute",
        position=[0, 0.5, -0.5]
    )

# Link6 (relative to Link5_Link6)
    pyrosim.Send_Cube(
        name="Link6",
        pos=[0, 0, -0.5],
        size=[1, 1, 1]
    )

    # Link6 -> Link7 (down)
    pyrosim.Send_Joint(
        name="Link6_Link7",
        parent="Link6",
        child="Link7",
        type="revolute",
        position=[0, 0, -0.5]
    )

    pyrosim.Send_Cube(
        name="Link7",
        pos=[0, 0, -1.0],
        size=[1, 1, 1]
    )
    pyrosim.End()
Create_World()
Create_Robot()
