import numpy as np

v = np.random.rand(10)
print(v)

normalized_v = v / np.sqrt(np.sum(v**2))
print(normalized_v)