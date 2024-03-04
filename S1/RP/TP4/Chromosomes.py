import numpy as np
import random

class Chromosome:
    def __init__(self, seq = None):
        if seq == None : 
            self.sequence = list()
            for i in range(N_QUEENS):
                self.sequence.append(random.randint(0, N_QUEENS-1))
        else: 
            self.sequence = seq
        self.fitness = None

    def setFitness(self):
        horizontal_collisions = 0
        for i in range(0, N_QUEENS-1):
            for j in range(i+1, N_QUEENS):
                if self.sequence[i] == self.sequence[j]:
                    horizontal_collisions += 1
        
        diagonal_collisions = 0
        for i in range(0, N_QUEENS-1):
            for j in range(i+1, N_QUEENS):
                if abs(i-j) == abs(self.sequence[i]-self.sequence[j]):
                    diagonal_collisions += 1
        self.fitness = (N_QUEENS*( N_QUEENS-1)/2) - (horizontal_collisions + diagonal_collisions)

    def mutate(self):
        
        p = random.uniform(0,1)
        if p < MUTATE_PROB:
            col = random.randint(0, N_QUEENS-1)
            self.sequence[col] = random.randint(0, N_QUEENS-1)


def generateInitialPopulation():

    population = list()
    for i in range(POPULATION_SIZE):
        chromosome = Chromosome()
        population.append(chromosome)
        chromosome.setFitness()
    return population


def elitism(population):

    sortedPopulation = sorted(population ,key=lambda chrom: chrom.fitness, reverse=True)   
    newPopulation = list()
    newPopulation.append(sortedPopulation[0])
    newPopulation.append(sortedPopulation[1])
    return newPopulation



def rouletteWheelSelection(population):

    # Compute the sum of the fitness scores of the whole population
    sumFitness = 0
    for chrom in population:
        sumFitness += chrom.fitness
    # Compute the survival probability of each chromosome in the population
    survivalProbs = list()
    for chrom in population:
        survivalProbs.append(chrom.fitness/sumFitness)
    # Compute the cumulative survival probabilities
    cumSurvivalProbs = np.cumsum(survivalProbs)
    # Generate a random probability
    p = random.uniform(0,1)
    # Select a chromosome with a cumulative probability >= p
    for i in range(POPULATION_SIZE):
        if cumSurvivalProbs[i] >= p:
            return population[i]



def crossover(parent1 , parent2):
    sequence = list()
    for i in range(N_QUEENS):
        p = random.uniform(0,1)
        if p < 0.5:
            sequence.append(parent1.sequence[i])
        else:
            sequence.append(parent2.sequence[i])
    
    newChrom = Chromosome(sequence)
    newChrom.setFitness()
    return newChrom


def GA(population, maxFitness):

    newPopulation = elitism(population)
    for i in range(POPULATION_SIZE-2):
        parent1 = rouletteWheelSelection(population)
        parent2 = rouletteWheelSelection(population)
        
        
        child = crossover(parent1, parent2)
        if MUTATE_FLAG :
            child.mutate()
        newPopulation.append(child)
        if child.fitness == maxFitness:
            break
    return newPopulation


# Global variables
N_QUEENS = 8
POPULATION_SIZE = 100
MUTATE_FLAG = True
MUTATE_PROB = 0.1
MAX_ITER = 1000


def Main():
    maxFitness = N_QUEENS * (N_QUEENS-1) /2
    population = generateInitialPopulation()

    generation = 1
    while  (maxFitness != max(population, key=lambda chrom: chrom.fitness).fitness) and (generation <= MAX_ITER):
        population = GA(population, maxFitness)
        generation += 1
    
    bestChromosome = max(population, key=lambda chrom: chrom.fitness)
    if bestChromosome.fitness == maxFitness:
        print ('Game solved in generation: ', generation-1)
        print ('Solution: ', bestChromosome.sequence)
    else:
        print ('Game not solved. Best fitness: ', bestChromosome.fitness)
        print ('One of the best solution: ', bestChromosome.sequence)

Main()