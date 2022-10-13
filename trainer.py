import random as random


class Trainer:
    """Class to interface with the tetris game
        Generates the epochs and deals with the

    Population formatting:
    pop = {
      1 : (child number) {
          "modifier":[Aggregate height, complete height, holes, Bumpiness]
      } end of child
      ... Repeat children for size
      "seed":"seed of the epoch"
      "epoch": "generation of the population"
    }

    """

    def __init__(self):
        self.fitness = None
        self.seed = None

    def __int__(self, generation, population=None, size=50):
        # set the population to an empty dict by default
        if population is None:
            population = []

        self.population = population
        """list of children for an epoch (2d list)"""
        self.size = size
        """The size of the population (default 50)"""
        self.generation = generation
        """The epoch generation (nice to have)"""

    def gen_epoch(self, new_seed):
        """Create new epoch"""
        self.seed = new_seed
        """The seed of the epoch (used for playback of the epoch)"""
        new_population = []
        # Find the best for parents
        # Keep the parents?
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
            # Stop if we reach the end of an odd length
            stop = (i1 == index_len)
            if stop:
                break

            i2 = 2 * x + 1
            parent2 = self.population[i2]

            modifier1, modifier2 = cross_breed(parent1, parent2)

            # Cross-breed children
            # Mutate the children
            new_population.append(modifier1)  # the list of modifiers
            new_population.append(modifier2)

        return  # EOF

    def get_population(self):
        """Retrieve the epoch info list"""
        return self.population

    def get_mods(self, child_num):
        """Retrieve the modifiers of one of the children"""
        assert child_num < self.size, f"Tried to get a modifier from a child that does not exist: {child_num}"

        return self.population[child_num]["modifier"]  # list of mod from population

    def calc_fitness(self, child_num, score, cleared_lines, ):
        """fitness function??? evaluate the result of a child and store the fitness value into the fitness list"""

    def get_best(self):
        """Retrieve the data for the best of this epoch
            Note: The whole epoch must be tested to get the true best
            (Maybe insert test to check)
            Returns: Seed, Modifiers"""


def mutate(modifiers):
    """Mutate the population (part of the gen_epoch function)
        Returns: the list of modifiers"""
    rand_pos = random.randint(0, 3)
    rand_offset = random.random()
    modifiers[rand_pos] += rand_offset
    return modifiers


def cross_breed(parent_mod1, parent_mod2):
    """Take the two parent modifiers and cross-breed them to get 2 new modifiers
            Returns: a list of two modifiers"""

    new_parent_mod1 = [parent_mod1[0], parent_mod1[1], parent_mod2[2], parent_mod2[3]]
    new_parent_mod2 = [parent_mod2[0], parent_mod2[1], parent_mod1[2], parent_mod1[3]]

    return new_parent_mod1, new_parent_mod2
