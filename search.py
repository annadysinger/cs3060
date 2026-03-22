import sys
print(sys.executable)
print("search")
from hillclimber import HILL_CLIMBER

hc = HILL_CLIMBER()
hc.Evolve()
hc.Show_Best()
