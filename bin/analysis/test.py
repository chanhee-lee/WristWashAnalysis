import numpy as np
from scipy.spatial.distance import euclidean

from fastdtw import fastdtw

x = np.array([[1,1], [12,12], [3,3], [21,21]])#, [4,4], [5,5]])
y = np.array([[2,2], [6,6], [2,2], [8,8]])
distance, path = fastdtw(x, y, dist=euclidean)
print(distance)
print(path)

