"""A Python implementation of NEAT (Neuroevolution of augmenting topologies)"""

import configuration as configuration #pylint: disable=import-error
import CUDA_Utils as CUDA_Utils #pylint: disable=import-error
import Math_Utils as Math_Utils #pylint: disable=import-error

from activations import ActivationFunctions #pylint: disable=import-error
from aggregations import AggregationFunctions #pylint: disable=import-error

configuration.validate_config()
Math_Utils.CUDA_Math_Utils.add_numbers_to_list()