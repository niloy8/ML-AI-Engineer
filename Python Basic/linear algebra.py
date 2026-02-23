import numpy as np
theta = np.pi / 2   # 90 degrees

rotation_z = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

point = np.array([1,0,0])

new_point = rotation_z @ point
print(new_point)