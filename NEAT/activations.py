"""
Contains the built-in activation functions
and code for adding and using them.
"""
import numpy as np
import types
import sys

class ReLUs(object):
    @staticmethod
    def Normal(z):
        return z if z > 0.0 else 0.0
    @staticmethod
    def Leaky(z):
        return z if z > 0.0 else z * 0.01
    @staticmethod
    def Parametric(z, a):
        return z if z > 0.0 else z * a

def softmax(z):
    return np.exp(z) / np.sum(np.exp(z), axis=0)

class InvalidActivationError(TypeError):
    pass

def Validate_Act(name, func):
    funcInstances = (
        types.BuiltinFunctionType,
        types.FunctionType,
        types.LambdaType
    )
    if not isinstance(name, str):
        raise InvalidActivationError("Name must be a string.")
    if not isinstance(func, funcInstances):
        raise InvalidActivationError("A function object is required.")
    if not (func.__code__.co_argcount >= 1):
        raise InvalidActivationError("A function with atleast one argument is required.")

class ActivationFunctions(object):
    """Contains all the built-in activation functions and functions to add and retrieve them."""
    def __init__(self):
        self.funcs = {}
        self.add("Parametric ReLU", ReLUs.Parametric)
        self.add("Leaky ReLU", ReLUs.Leaky)
        self.add("ReLU", ReLUs.Normal)
        self.add("Softmax", softmax)
    def get(self, name):
        if name in self.funcs:
            return self.funcs[name]
        else:
            raise InvalidActivationError('Activation function "%s" not found.' % name)
    def add(self, name, func):
        Validate_Act(name, func)
        if name in self.funcs:
            raise InvalidActivationError('Activation function "%s" already exists.' % name)
        else:
            self.funcs[name] = func