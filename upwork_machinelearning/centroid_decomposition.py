import numpy as np
from numpy import linalg as LA
import threading


def SSV(x, n, m):
    pos = 0
    while pos == 0:
        if pos == 0:
            Z = np.ones(shape=(n, 1))
        else:
            Z[pos] == -Z[pos]
        for i in range(n+1):
            S = 0
            for i in range(n):
                sem_res = np.dot(Z[i][0], x[i].T)
                S += sem_res
            V = []
            for i in range(n):
                v = LA.norm(np.dot(Z[i][0], (np.dot(Z[i][0], x[i]*S) - np.dot(x[i], x[i].T))))
                V.append(v)
            print(V)
            val = 0
            for i in range(n):
                if np.dot(Z[i], V[i]) < 0:
                    if np.abs(V[i]) > val:
                        val = V[i]
                        pos = i
        return Z


# Calculate centroid decomposition
def centroid_decomposition(x):
    print("x = ", x)
    n = x.shape[0]
    print("n = ", n)
    m = x.shape[1]
    print("m = ", m)
    L = R = []
    for i in range (0, m):
        z = SSV(x,n,m)
        r = (np.transpose(x)*z)/LA.norm(np.transpose(x)*z)
        l = x*r
        if i==0:
            R=r
            L=l
        else:
            R=np.c_[R,r]
            L=np.c_[L,l]
        x = x - l*np.transpose(r)
    return L,R


input_matrix = []
with open("./senate_votes.txt") as f:
    for line in f:
        current_row = [int(x) for x in line.strip().split(' ')]
        input_matrix.append(current_row)

input_matrix = np.matrix(input_matrix)

L, R = centroid_decomposition(input_matrix)

print("L= " + str(L))
print("R=" + str(R))

