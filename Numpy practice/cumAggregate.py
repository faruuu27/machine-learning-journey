import numpy as np

arr=np.array([20,30,40,50])

print(np.cumsum(arr))
print(np.cumprod(arr))

arr2=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]]
               )

print(arr2.mean(axis=1))
   # axis=1 colappes the rows [1+5+9/3]
