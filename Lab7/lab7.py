import numpy as np
coeff_matrix = np.array([
    [-1, 0.8, -0.15],
    [0.8, -1.15, 0],
    [-0.15, -0.8, -1]
])
soln= np.array([-15.58, 3.3, 0])
gamma = np.linalg.solve(coeff_matrix, soln)
print(gamma)

coeff_matrix = np.array([
    [-gamma[0], -gamma[1]],
    [-gamma[1], -gamma[0]]
])
soln= np.array([gamma[1], gamma[2]])

a_2 = np.linalg.solve(coeff_matrix, soln)
print(">>",a_2)
