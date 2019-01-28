"""
Contains the configuration variable and
the functions to validate it.
"""
import types
from random import random

class config(object): #read the documentation in the docs folder for more information.
    #population
    class population(object):
        population_size = 50
    
    #computation
    class computation(object):
        use_cuda = True
        use_fixed_chunks = False
        chunking_function = "nearest_to_divisible" #has to be a name of a built-in function or a function object.
        max_chunk_size = 200
        min_chunk_size = 0.5

    #fitness functions
    class fitness(object):
        """
        test_if_better: test if criterion return correlates with the overall fitness of a list.
        """
        fitness_criterion = max
        test_if_better = True

class InvalidCriterionError(TypeError):
    pass

def validate_config():
    test_criterion()

def test_criterion():
    criterion = config.fitness.fitness_criterion
    funcInstances = (
        types.BuiltinFunctionType,
        types.FunctionType,
        types.LambdaType
    )
    if not isinstance(criterion, funcInstances):
        raise InvalidCriterionError("A function object is required.")
    randomList = [round((random() * 10), 1) for _ in range(10)]
    try:
        criterion(randomList)
    except Exception:
        raise InvalidCriterionError("The function must be able to process lists.")
    typeList = (
        int,
        float
    )
    if not isinstance(criterion(randomList), typeList):
        if not isinstance(criterion(randomList), complex):
            raise InvalidCriterionError("The function must return a real number.")
        else:
            raise InvalidCriterionError("The function must return a REAL number.")
    if config.fitness.test_if_better:
        relation = "none"
        for _ in range(10):
            randomWorseList = [round((random() * 10), 1) for _ in range(10)]
            randomInt = round(random() * 10, 1)
            randomBetterList = [x + randomInt for x in randomWorseList]
            if randomWorseList < randomBetterList:
                newRelation = "asc"
            elif randomWorseList > randomBetterList:
                newRelation = "desc"
            else:
                raise InvalidCriterionError("The function must return different values for different inputs")
            if relation == "none":
                relation = newRelation
            else:
                if relation != newRelation:
                    raise InvalidCriterionError("The functions output with two different lists must correlate to the overall fitness of the lists")