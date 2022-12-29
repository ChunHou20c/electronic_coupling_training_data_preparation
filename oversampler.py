"""
This module will do a oversampling by making possible permutations from the colomb matrix
"""
import numpy as np

def isomorphic_matrix(coulomb_matrix:np.ndarray, size:int, n:int, is_pair:bool = True):
    """
    This function generate n permutation of colomb matrix
    """
    
    #first generate the sequence for the permutation
    
    numbers = np.arange(size)

    list_to_return = []

    if is_pair :
        
        for _ in range(n):
            random_order = np.random.permutation(numbers)
            random_order = np.concatenate((random_order, random_order + size))
            permutated_cm = coulomb_matrix[random_order][:,random_order]
            list_to_return.append(permutated_cm)
    
    return list_to_return
    
def normal_noise(coulomb_matrix:np.ndarray, size:int, shape:tuple, standard_deviation:float = 0.5):
    """
    this function add a normal noise to the coulomb matrix by randomly generated noise
    increase standard deviation to make higher noise
    """

    
    cm_list = []
    for _ in range(size):
        
        random_noise = np.random.normal(100, standard_deviation, shape)
        altered_cm = random_noise*coulomb_matrix/100

        cm_list.append(altered_cm)
    
    return cm_list


