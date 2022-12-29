"""
This script delete unwanted element from the coulomb matrix
"""
import numpy as np


H_index = [0,3,8,10,13,17,19,23,25,28,30,33,34,35,38,40,45,47,49,51,55]
C_index = [32]
O_index = [31]

index_removal = np.array(H_index + C_index + O_index)
pair_index_removal = np.concatenate((index_removal, index_removal+56))

print(len(index_removal))

matrix = np.load('cleaned_cm_positive/matrix.npy')

reduced_matrix_list = []
for i in matrix:

    reduced_matrix = np.delete(i, pair_index_removal, axis=0)
    reduced_matrix = np.delete(reduced_matrix, pair_index_removal, axis=1)
    
    reduced_matrix_list.append(reduced_matrix)

print(reduced_matrix_list[0].shape)
print(len(reduced_matrix_list))

np.save('cleaned_cm_positive/reduced_matrix.npy', reduced_matrix_list)
