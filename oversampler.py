"""
This module will do a oversampling by making possible permutations from the colomb matrix
"""
import numpy as np
import itertools

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
    

matrix = np.load('cleaned_cm_positive/matrix.npy')

ls = isomorphic_matrix(matrix[0],56,230,True)

for cm1, cm2 in itertools.combinations(ls,2):

    if(np.array_equal(cm1, cm2)):

        print('duplication found')

print(len(ls))
