import numpy as np

array = np.array([1,2,3])

# scalar arithmetic

print(array+1)  # [2 3 4]
print(array-1)  # [0 1 2]
print(array*2)  # [2 4 6]
print(array/2)  # [0.5 1.  1.5]
print(array**3)  # [ 1  8 27]


# element wise arithmetic 

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
#basically all the + - * ** .... operation done with these 2 arrays will be done element by elemenet
  


# comparaison (easy stuff tbh ) 

scores = np.array([85,67,55,94,100,79])

print(scores==100)
print(scores >= 60)
scores[scores<60] = 0
scores[scores>= 60]= 1
print(scores)