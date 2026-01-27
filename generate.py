import pyrosim.pyrosim as pyrosim

# Start SDF file
pyrosim.Start_SDF("boxes.sdf")

# Tower parameters
tower_height = 10       # number of blocks per tower
num_rows = 5            # towers along x-axis
num_columns = 5         # towers along y-axis
initial_length = 1
initial_width = 1
initial_height = 1
spacing = 2             # space between towers

# Loop over each tower in the grid
for row in range(num_rows):
    for col in range(num_columns):
        # Reset size for each tower
        length = initial_length
        width = initial_width
        height = initial_height
        
        # Base position for this tower
        x = row * spacing
        y = col * spacing
        z = height / 2   # bottom of first cube sits on floor
        
        # Build the tower vertically
        for i in range(tower_height):
            pyrosim.Send_Cube(
                name=f"Block_r{row}_c{col}_i{i}",
                pos=[x, y, z],
                size=[length, width, height]
            )
            # Prepare next block
            z += height       # stack vertically
            length *= 0.9     # shrink each level
            width *= 0.9
            height *= 0.9

# End SDF file
pyrosim.End()



