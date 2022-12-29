usage of random noise:

```
matrix:np.ndarray #this is your matrix data
coupling:np.ndarray #this is coupling

new_feature, new_coupling = gen_noisy_dataset(matrix, coupling, duplication_count = 100)

#then use new_feature and new_coupling to train model
```
