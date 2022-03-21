import numpy as np
import math
def NormalizeData(data):
     return math.floor(math.log10(data)+1)

X = np.array([
    [ 0,  1],
    [ 2,  3],
    [ 4,  5],
    [ 6,  7],
    [ 8,  9],
    [10, 11],
    [12, 13],
    [14, 15],
    [14, 15000]
])

scaled_x = NormalizeData(X)

print(scaled_x)