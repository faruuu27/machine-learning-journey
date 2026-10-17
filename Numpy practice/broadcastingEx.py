import numpy as np

vector=np.array([10])

matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(vector.shape) #(3,)
                    #(3, 3)
print(matrix.shape)
# array2=np.ones((2,1),dtype=str)
# print(array2)

print(matrix +vector)
print(vector+matrix)