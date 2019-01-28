"""
Contains the built-in aggregation functions
and code for adding and using them.
"""
import numpy as np
import sys
import types
from operator import mul

if sys.version_info[0] > 2:
    from functools import reduce

def product_aggr(x):
    return reduce(mul, x, 1.0)

def sum_aggr(x):
    return sum(x)

def max_aggr(x):
    return max(x)

def min_aggr(x):
    return min(x)

class InvalidAggregationError(TypeError):
    pass

def Validate_Aggr(name, func):
    funcInstances = (
        types.BuiltinFunctionType,
        types.FunctionType,
        types.LambdaType
    )
    if not isinstance(name, str):
        raise InvalidAggregationError("Name must be a string.")
    if not isinstance(func, funcInstances):
        raise InvalidAggregationError("A function object is required.")
    if not (func.__code__.co_argcount >= 1):
        raise InvalidAggregationError("A function with atleast one argument is required.")

class AggregationFunctions(object):
    """Contains all the built-in aggregation functions and functions to add and retrieve them."""
    def __init__(self):
        self.funcs = {}
        self.add("Product", product_aggr)
        self.add("Sum", sum_aggr)
        self.add("Max", sum_aggr)
        self.add("Min", min_aggr)
    def get(self, name):
        if name in self.funcs:
            return self.funcs[name]
        else:
            raise InvalidAggregationError('Aggregation function "%s" not found.' % name)
    def add(self, name, func):
        Validate_Aggr(name, func)
        if name in self.funcs:
            raise InvalidAggregationError('Aggregation function "%s" already exists.' % name)
        else:
            self.funcs[name] = func