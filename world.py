import pybullet as p
class WORLD:

    def __init__(self):
        # Load ground plane
        self.planeId = p.loadURDF("plane.urdf")

        # Load world description
        p.loadSDF("world.sdf")
