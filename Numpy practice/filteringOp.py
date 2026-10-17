import numpy as np

arr=np.array([[1,2,3,4,5,6],
             [7,8,9,10,11,23]])


#and
print(arr[(arr<10) & (arr>5)])
print(arr[(arr<10) | (arr>5)])
print(arr[~(arr<5)])

