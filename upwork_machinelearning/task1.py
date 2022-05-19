import numpy as np
from numpy.linalg import svd

# creating matrix by reading file senate_votes.txt
input_matrix = []
with open("./senate_votes.txt") as f:
    for line in f:
        current_row = [int(x) for x in line.strip().split(' ')]
        input_matrix.append(current_row)
    f.close()

matrix = np.matrix(input_matrix)

U, SVD, VT = svd(matrix)

print('This is U matrix: \n', U, '\n')
print('It has a shape: \n', U.shape, '\n\n\n')
print('This is SVD matrix: \n', SVD, '\n')
print('It has a shape: \n', SVD.shape, '\n\n\n')
print('This is VT matrix: \n', VT, '\n')
print('It has a shape: \n', VT.shape)
