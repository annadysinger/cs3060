print("parallelhillclimber")
from solution import SOLUTION
import constants as c
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        import os
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")
        print("populationSize =", c.populationSize)   
        self.nextAvailableID = 0
#        print("init")
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1      
       # print(self.parents)
    def Evolve(self):
        print("evolve start")
        print("parents at evolve:", self.parents)
        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")
            self.parents[i].Wait_For_Simulation_To_End()
        for generation in range(c.numberOfGenerations):

            print("\nGeneration:", generation)
            self.Spawn()
            self.Mutate()
            self.Evaluate_Children()
            self.Select() 

    def Show_Best(self):
      #  self.parent.Evaluate("GUI")
        best = max(self.parents.values(), key=lambda s: s.fitness)

        best.Start_Simulation("GUI")
    def Mutate(self):

        for i in self.children:
            self.children[i].Mutate()

    def Spawn(self):

        self.children = {}

        for i in self.parents:

            self.children[i] = self.parents[i].Copy()
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
    def Evaluate_Children(self):

        for i in self.children:
            self.children[i].Start_Simulation("DIRECT")
            self.children[i].Wait_For_Simulation_To_End()
    def Select(self):

        for i in self.parents:
            
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]
