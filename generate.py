import pyrosim.pyrosim as pyrosim

# Start SDF file
pyrosim.Start_SDF("world.sdf")  # minimal world

# One cube at origin
length = 1
width = 1
height = 1
x = 0
y = 0
z = height / 2   # bottom sits on floor

pyrosim.Send_Cube(name="Block", pos=[x, y, z], size=[length, width, height])
# End SDF file
pyrosim.End()



