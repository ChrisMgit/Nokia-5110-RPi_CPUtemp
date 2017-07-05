import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.ion()
fig = plt.figure()
axis = Axes3D(fig)

a1 = np.array([0, 0, 0])

for i in range(100):
    plt.hold(True)
    a = np.random.rand(i, 3)
    a1 = np.append(a, a1)
    axis.scatter(a1[0], a1[1], a1[2])
    plt.pause(0.0001)
    plt.ioff()
    plt.show(block=False)
