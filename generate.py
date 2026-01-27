import pyrosim.pyrosim as pyrosim

# Start SDF file
pyrosim.Start_SDF("boxes.sdf")

# --- Tower parameters ---
length = 1
width = 1
height = 1

# Position for the first block
x = 0
y = 0
z = height / 2   # sits on floor

num_blocks = 10

for i in range(num_blocks):
    pyrosim.Send_Cube(name=f"Block{i+1}", pos=[x, y, z], size=[length, 
width, height])
    
    # Prepare for next block
    z += height      # stack on top
    length *= 0.9    # reduce size
    width *= 0.9
    height *= 0.9

# --- Optional extra cube in front of tower ---
length2 = 1
width2 = 1
height2 = 1
x2 = 0
y2 = 1.5
z2 = height2 / 2   # bottom on floor

pyrosim.Send_Cube(name="Box2", pos=[x2, y2, z2], size=[length2, width2, 
height2])

# End SDF file
pyrosim.End()

