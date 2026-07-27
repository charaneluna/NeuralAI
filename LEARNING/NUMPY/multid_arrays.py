import numpy as np

array = np.array([
                    [[ 'A', 'B' , 'C'],[ 'D', 'E', 'F'], ['G', 'H', 'I']],
                    [[ 'J', 'K' , 'L'],[ 'M', 'N', 'O'], ['P', 'Q', 'R']],
                    [[ 'S', 'T' , 'U'],[ 'V', 'W', 'X'], ['Y', 'Z', ' ']]

                                                                ])

print(array.ndim) # dimension of array
print(array.shape) # (3,3,3) 3depth 3 rows 3 columns
# in usual arrays in python we would do chain indexing which is like the following : 
# array[0][0][0], but in nympy we use multidimentional indexing (faster)
print(array[2,0,0])
print(int(array[2,0,0])+ int(array[2,1,2])) # bc the first elements of the array are str the intire thing turned into str
