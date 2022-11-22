import random as random


class Trainer:
    """Class to interface with the tetris game
        Generates the epochs and deals with the

    Population formatting:
    modifier = [Aggregate height, complete height, holes, Bumpiness]
    """
    def __init__(self): # default constructor (I think that is how this works)
            self.seed = None
            """The seed of the epoch because why not"""
            # All of this code is for defining the varibles with text when hovered over (just ignore)
            self.fitness = []
            """The list of fitness scores assigned to each child
                Note: The list is already creted so the saved values can be saved via the child_num as the index"""
            self.population = None
            """The list of children (modifiers) for an epoch (2d list)"""
            self.size = 50
            """The size of the population (default 50)"""
            self.generation = 0
            """The epoch generation (nice to have for saving data)"""
            self.max_mute = 0.1
            """The max size that the mutation function will change a value"""
            self.norm_size = 1
            """The sum total of the modifier list (default 1)"""

    def __int__(self, generation:int=0, population:list=None, size=50, max_mute:float=0.1, norm_size:int=1, seed:int=None):
         # Set the variables to the varibles
        # Auto generate the fitness list
        self.fitness = [] * size
        """The list of fitness scores assigned to each child
            Note: The list is already creted so the saved values can be saved via the child_num as the index"""
        self.population = population
        """The list of children (modifiers) for an epoch (2d list)"""
        self.size = size
        """The size of the population (default 50)"""
        self.generation = generation
        """The epoch generation (nice to have for saving data)"""
        self.max_mute = max_mute
        """The max size that the mutation function will change a value"""
        self.norm_size = norm_size
        """The sum total of the modifier list (default 1)"""
        self.set_seed(seed)
        """The seed of the epoch because why not"""

    def gen_epoch(self, new_seed:int=None):
        """Create new epoch"""
     
        #region setup
        # create a new population of the next epoch
        new_population = []

        # By default find a seed for the epoch
        self.set_seed(new_seed)
        
        # feel free to comment this line out
        random.seed(new_seed) 
        
        #endregion
        
        # If there is no current population then make one up
        if self.population is None:
            # for the size of the population
            for i in range(self.size):
                
                # create a new child
                new_child = self.gen_mod_rand()
            
                # add the child to the population
                new_population.append(new_child)
            
            # If there was no population then stop when one is made
            self.population = new_population
            return
        
        #region parents
        # Find the best children to become parents
        fit_avg = sum(self.fitness) / len(self.fitness)
        index = [] # A list of the index for parents
        
        # Find all the best parents
        for i in range(len(self.fitness)):
            # Check to make sure that we don't go over half the population size
            if i > self.size:
                # Stop if you go over
                break
            if self.fitness[i] > fit_avg:
                index.append(i)
        #endregion
        
        index_len = len(index)
        assert index_len == len(self.fitness) // 2, f"oop {index_len} {len(self.fitness)}"
        # Start the Gen
        for x in range(index_len):

            i1 = 2 * x
            parent1 = self.population[i1]
            # add the parent back into the population
            new_population.append(parent1)
            # Stop if we reach the end of an odd length 
            # therefore there is not a second parent to cross breed with
            if i1 >= index_len:
                # I geuss just mutate the parent
                modifier = self.mutate(parent1)
                new_population.append(modifier)
                break

            i2 = i1 + 1
            parent2 = self.population[i2]

            # Cross-breed (includes mutation and normalizing) children
            modifier1, modifier2 = self.cross_breed(parent1, parent2)
            
            # Add the children to the population
            new_population.append(modifier1)
            new_population.append(modifier2)
        
        # if stopped only add one to the population
          
        
        # Random check to ensure that the population is the correct size
        # I will comment out for testing to see if everything else works but this is a lazy band-aid if needed   
        if not len(new_population) == self.size:
            print(f"The size of the population did not generate correctly: {len(new_population)} created of max {self.size} \n oops :(")

            while len(new_population) > self.size:
                print("removing a child")
                new_population.pop()
                
            while len(new_population) < self.size:
                print("adding a child")
                new_population.append(self.gen_mod_rand)    
        # Maybe put in a useless if statement to generate any missing (Shouldn't need but like idk)
        
        # Set the new population as the population
        self.population = new_population
            
        return  # EOF
    
    def cross_breed(self, parent_mod1:list, parent_mod2:list):
        """Take the two parent modifiers and cross-breed them to get 2 new modifiers
                Returns: a list of two modifiers"""
        # safety assert
        assert len(parent_mod1) == 4 and len(parent_mod2) == 4, f"Cannot cross breed modifiers that are invalid length: {parent_mod1} & {parent_mod2}"
        
        new_mod1 = [parent_mod1[0], parent_mod1[1], parent_mod2[2], parent_mod2[3]]
        new_mod2 = [parent_mod2[0], parent_mod2[1], parent_mod1[2], parent_mod1[3]]
        
        # Then mutate the children for diversity
        new_mod1 = self.mutate(new_mod1)
        new_mod2 = self.mutate(new_mod2)   
        
        # Then normalize the modifiers to have a sum of 1
        new_mod1 = self.normalize(new_mod1)
        new_mod2 = self.normalize(new_mod2) 

        return new_mod1, new_mod2
    
    def mutate(self, modifiers:list):
        """Mutate the population (part of the gen_epoch function)
            Returns: the list of modifiers"""
        
        # Randomly change one of the modifiers by a bit 
        rand_pos = random.randint(0, 3)
        rand_offset = random.uniform(-1,1)
        rand_offset = self.max_mute * rand_offset # limit the size of the modification
        modifiers[rand_pos] += rand_offset
        
        return modifiers


    def normalize(self, v:list):
        """Convert the vector to have a total of norm_size(defalut=1)
            Note: if the sum is 0 a new vector is created"""
        total = sum(v)
        
        # Catch the possiblity that the vector if the 0 vector
        # This could affect the evaluation function
        if total == 0:
            v = self.gen_mod_rand()
            total = sum(v)
        
        # normalize to sum of norm_size
        for x in range(len(v)):
            v[x] = self.norm_size*(v[x] / total)

        return v

    def gen_mod_rand(self, size=4):
        """Generate a list of 4 modifiers randomly"""
        modifiers=[]
        for x in range(size):
            modifiers.append(random.randrange(1,10))
        modifiers = self.normalize(modifiers)
        
        return modifiers
               

    def get_population(self):
        """Retrieve the epoch info list"""
        return self.population

    def get_mods(self, child_num):
        """Retrieve the modifiers of one of the children"""
        assert child_num < self.size, f"Tried to get a modifier from a child that does not exist: {child_num}"

        return self.population[child_num]  # list of mod from population
    
    def get_seed(self):
        return self.seed

    def set_seed(self, seed:int = None):
        if seed == None:
            seed = self.gen_seed()
        self.seed = seed
        random.seed(seed)
    
    def gen_seed(self):
        return random.randrange(1000,9999)

    def calc_fitness(self, child_num, score, cleared_lines, ):
        """fitness function: evaluate the result of a game and store the fitness value into the fitness list"""
        fit_val = 1 # 

    def get_best(self):
        """Retrieve the data for the best of this epoch to save
            Note: The whole epoch must be tested to get the true best
            (Maybe insert test to check)
            Returns: Seed, Modifiers"""
        
        best_fit:int = max(self.fitness) # The fitness score of the best child    
        best_index = self.fitness.index(best_fit) # The index of the best child  
        best_mod:list = self.population # The modifiers of the best child
        
        return {
            "seed":self.seed,
            "modifiers":best_mod,
            "child number":best_index,
            "generation":self.generation
            }
        