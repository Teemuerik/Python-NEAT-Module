"""
Contains the functions used to divide the population into chunks
that are computed by the GPU in parallel.
"""

from Math_Utils import CUDA_Math_Utils as utils #pylint: disable=import-error
import configuration as configuration #pylint: disable=import-error

config = configuration.config.computation
pop_count = configuration.config.population.population_size

class chunking_functions(object):
    class automatic_size(object):

        @staticmethod
        def nearest_to_divisible():
            self = chunking_functions.automatic_size
            utils.get_min_remainder

    class fixed_size(object):
        pass