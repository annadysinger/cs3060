import sys
print(sys.executable)
print("search")
from parallelHillClimber import PARALLEL_HILL_CLIMBER
print("before constructor")
phc = PARALLEL_HILL_CLIMBER()
print("before evolve")
phc.Evolve()
print("after evolve")
phc.Show_Best()
print("done")

