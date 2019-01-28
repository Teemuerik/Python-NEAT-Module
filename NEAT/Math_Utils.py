"""Contains custom mathematical functions used in CUDA functions"""
from math import floor, ceil
from configuration import config as configuration #pylint: disable=import-error

def_config = configuration.computation
def_pop_size = configuration.population.population_size

num_list = []
divisible_list = []

class CUDA_Math_Utils(object):
    @staticmethod
    def add_numbers_to_list(config=def_config, pop_size=def_pop_size):
        self = CUDA_Math_Utils
        temp_num_list = []
        max_chunks = config.max_chunk_size
        for a in range(2, max_chunks):
            if a in divisible_list:
                pass
            else:
                for b in range(2, floor(pop_size / a)):
                    divisible_list.append(a * b)
        temp_num_list.extend([ln for ln in [n for n in range(2, pop_size) if n not in divisible_list] if self.number_meets_requirements(ln)])
        num_list.extend(self.expand_number_list(temp_num_list))
        print(num_list)

    @staticmethod    
    def get_min_remainder(config=def_config, pop_size=def_pop_size):
        self = CUDA_Math_Utils
        chunk_max = config.max_chunk_size
        if not any(num_list) and (0 not in num_list):
            self.add_numbers_to_list()
        min_return = ((pop_size - pop_size % num_list[0]) / num_list[0], pop_size % num_list[0], (pop_size - pop_size % num_list[0]) / ((pop_size - pop_size % num_list[0]) / num_list[0]))
        valid_return = round(min_return[2]) == min_return[2]
        if pop_size % chunk_max == 0.0:
            return (chunk_max, 0.0, pop_size / chunk_max)
        for a in num_list:
            if pop_size % a == 0.0:
                return (pop_size / a, 0.0, a)
            else:
                A = min_return
                B = ((pop_size - pop_size % a) / a, pop_size % a, (pop_size - pop_size % a) / ((pop_size - pop_size % a) / a))
                if valid_return:
                    if A[1] == B[1]:
                        if B[2] < A[2]:
                            min_return = B
                        else:
                            pass
                    else:
                        if B[1] == min(A[1], B[1]):
                            min_return = B
                        else:
                            pass
                else:
                    min_return = B
        return min_return
    
    @staticmethod
    def number_meets_requirements(num, config=def_config, pop_size=def_pop_size):
        max_chunks = config.max_chunk_size
        min_chunks = config.min_chunk_size
        bool1 = pop_size / num < max_chunks
        bool2 = False
        if max_chunks >= pop_size:
            bool2 = pop_size / num > pop_size * min_chunks
        else:
            bool2 = pop_size / num > max_chunks * min_chunks
        return bool1 and bool2
    
    @staticmethod
    def expand_number_list(l):
        self = CUDA_Math_Utils
        l_min = min(l)
        l_max = max(l)
        n_min = l_min
        n_max = l_max
        A = False
        B = False
        i = 0
        while not (A and B):
            if not A:
                if self.number_meets_requirements(l_min - i):
                    n_min = l_min - i
                else:
                    A = True
            if not B:
                if self.number_meets_requirements(l_max + i):
                    n_max = l_max + i 
                else:
                    B = True
            i += 1
        return list(range(n_min, n_max + 1))