# import numpy as np

# array = np.array([['A', 'B', 'C'],
#                  ['b', 'c', 'd']])

# print(array.shape)\


import numpy as np

rng = np.random.default_rng()

place = np.array(["Finland", "india", "bagladesh", "china", "usa", "russia", "nepal"])

place = rng.choice(place, size=(2, 2))

print(place)