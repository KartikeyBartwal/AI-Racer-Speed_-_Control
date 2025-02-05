import numpy as np

action = np.random.uniform(low=-1, high=1, size=(3,))  # Random action vector in the action space
action[2] = 0
print(action)
print(action[2])
