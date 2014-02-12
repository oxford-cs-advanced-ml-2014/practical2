import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import svd

X = plt.imread("YOUR_IMAGE.jpg").astype(np.float)
X /= 256.0
X = X.mean(axis=2) # make X black and white
plt.imsave("YOUR_IMAGE_IN_BLACK_AND_WHITE.jpg", np.dstack([X]*3))

# CODE GOES HERE
