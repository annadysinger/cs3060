print("hillclimber")
from solution import SOLUTION
import numpy
import constants as c
class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        import os
        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")   
        self.nextAvailableID = 0
#        print("init")
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1      
        self.fitnessValues = numpy.zeros((c.populationSize, c.numberOfGenerations))
       # print(self.parents)
    def Evolve(self):
        #print("evolve")
        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")
        for i in self.parents:
            self.parents[i].Wait_For_Simulation_To_End()
        for generation in range(c.numberOfGenerations):

            self.currentGeneration = generation
            print("\nGeneration:", generation)
            self.Spawn()
            self.Mutate()
            self.Evaluate_Children()
            self.Select() 
        numpy.save("fitnessValues.npy", self.fitnessValues)
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
        for i in self.children:
            self.children[i].Wait_For_Simulation_To_End()
    def Select(self):

        for i in self.parents:
            
            if self.children[i].fitness > self.parents[i].fitness:
                self.parents[i] = self.children[i]
            self.fitnessValues[i][self.currentGeneration] = self.parents[i].fitness
