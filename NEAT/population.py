from NEAT.configuration import config
from random import random
import types
import NEAT.reproduction

class population(object):
    """This class implements the core genetic algorithm."""
    
    def __init__(self, initial=None):
        self.fitness_criterion = config["fitness_criterion"]
        if initial is None:
            reproduction.create_random_gen(config["population_size"], )