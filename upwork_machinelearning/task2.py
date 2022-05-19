from centroid_decomposition import centroid_decomposition
import numpy as np

X = np.array([[2,-3], [1,6], [5,2]])

result = centroid_decomposition(X)

print(result)
