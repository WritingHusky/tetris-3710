import random as random
import numpy as np

def mutate(modifiers):
    """Mutate the population (part of the gen_epoch function)
        Returns: the list of modifiers"""
    rand_pos = random.randint(0, 3)
    rand_offset = random.random()
    modifiers[rand_pos] += rand_offset
    
    # Need to normalize these vectors
    
    return modifiers


def cross_breed(parent_mod1, parent_mod2):
    """Take the two parent modifiers and cross-breed them to get 2 new modifiers
            Returns: a list of two modifiers"""

    new_parent_mod1 = [parent_mod1[0], parent_mod1[1], parent_mod2[2], parent_mod2[3]]
    new_parent_mod2 = [parent_mod2[0], parent_mod2[1], parent_mod1[2], parent_mod1[3]]
    
    # Need to normalize these vectors or leave it to the mutate step?

    return new_parent_mod1, new_parent_mod2

def normalize(v: list):
    """Convert the vector to have a total of 1"""
    total = sum(v)
    if total == 0:
        return v

    for x in range(len(v)):
        v[x] = v[x] / total

    return v


class Trainer:
    """Class to interface with the tetris game
        Generates the epochs and deals with the

    Population formatting:
    modifier = [Aggregate height, complete height, holes, Bumpiness]
    """

    def __init__(self):
        self.fitness = None
        self.seed = None

    def __int__(self, generation, population=None, size=50):
        # set the population to an empty dict by default

        self.population = population
        """list of children for an epoch (2d list)"""
        self.size = size
        """The size of the population (default 50)"""
        self.generation = generation
        """The epoch generation (nice to have)"""

    def gen_epoch(self, new_seed):
        """Create new epoch"""
        # create a new population of the next epoch
        new_population = []
        
        self.seed = new_seed
        """The seed of the epoch (used for playback of the epoch)"""
        
        # If there is no current population then make one up
        if self.population is None:
            for i in range(self.size):
                new_child = []
                for y in range(4):
                    new_child.append(random.random())
                new_population.append(new_child)
        
        # Find the best for parents
        fit_cutoff = sum(self.fitness) / len(self.fitness)
        index = []
        """A list of the index for parents"""
        for i in range(len(self.fitness)):
            if self.fitness[i] <= fit_cutoff:
                index.append(i)

        index_len = len(index)
        # Start the Gen
        for x in (index_len // 2):

            i1 = 2 * x
            parent1 = self.population[i1]
            # add the parent back into the population
            new_population.append(parent1)
            # Stop if we reach the end of an odd length
            stop = (i1 is index_len)
            if stop:
                stop_parent = parent1
                break

            i2 = 2 * x + 1
            parent2 = self.population[i2]

            # Cross-breed children
            modifier1, modifier2 = cross_breed(parent1, parent2)

            # Mutate the children
            modifier1 = mutate(modifier1)
            modifier2 = mutate(modifier2) 
            
            # Add the children to the population
            new_population.append(modifier1)
            new_population.append(modifier2)
        
        # if stopped only add one to the population
        if stop:
            # I geuss just mutate the parent
            modifier = mutate(stop_parent)
            new_population.append(modifier)
            

        
            
        return  # EOF

    def get_population(self):
        """Retrieve the epoch info list"""
        return self.population

    def get_mods(self, child_num):
        """Retrieve the modifiers of one of the children"""
        assert child_num < self.size, f"Tried to get a modifier from a child that does not exist: {child_num}"

        return self.population[child_num]["modifier"]  # list of mod from population

    def calc_fitness(self, child_num, score, cleared_lines, ):
        """fitness function: evaluate the result of a game and store the fitness value into the fitness list"""
        fit_val = 1 # 

    def get_best(self):
        """Retrieve the data for the best of this epoch to save
            Note: The whole epoch must be tested to get the true best
            (Maybe insert test to check)
            Returns: Seed, Modifiers"""
            
        best_mod = None # The fitness score of the best child
        best_index = None # The index of the best child  
         
        for x in range(len(self.fitness)):
            current_mod = self.fitness[x]
            if current_mod > best_mod:
                best_mod = current_mod
                best_index = x
        
        
        return {}
    
    
vec = [1,1]
print(normalize(vec))
