import numpy as np
import matplotlib.pyplot as plt

y = np.zeros((10, 10))
for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            y[i][j] = 0
        else:
            y[i][j] = 1
plt.imshow(y)
plt.show()