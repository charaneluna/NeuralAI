import numpy as np

random = np.random.default_rng(seed=4)

# print(random.integers(low=1,high=100,size=(3,4)))


randomm = np.random.default_rng()
array = np.array([1,2,3,4])

randomm.shuffle(array)  # changes the position of numbers in the array

num = randomm.choice(array) # makes a random choice out of the array 

print(array)
print(num)