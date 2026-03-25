print("hillclimber")
from solution import SOLUTION
class HILL_CLIMBER:

    def __init__(self):
        print("init")
        self.parent = SOLUTION()
    def Evolve(self):
        print("evolve")
        self.parent.Evaulate("GUI")
        self.parent.Evaluate("DIRECT")
        for generation in range(10):

            print("\nGeneration:", generation)

            child = self.parent.Copy()

            child.Mutate()

            child.Evaluate("DIRECT")

            print("Parent:", self.parent.fitness, "Child:", child.fitness)
            
            if child.fitness > self.parent.fitness:

                print("Child wins! ")

                self.parent = child

    def Show_Best(self):
        self.parent.Evaluate("GUI")
