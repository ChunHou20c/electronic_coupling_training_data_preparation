usage of random noise:

```
matrix:np.ndarray #this is your matrix data
coupling:np.ndarray #this is coupling


modified_matrix = []
modified_matrix_coupling = []

for Matrix, Coupling in zip(matrix, coupling):
    
    duplication_count = 100
    noisy_matrices = normal_noise(Matrix, size = duplication_count, shape = Matrix.shape, standard_deviation = 0.5)
    list_of_generated_matrix = [Matrix] + noisy_matrices
    list_of_coupling = [coupling]*(duplication_count+1)
    
    modified_matrix += list_of_generated_matrix
    modified_matrix_coupling += list_of_coupling

feature = np.array(modified_matrix)
label = np.array(modified_matrix_coupling)
```
