import numpy as np

arr = np.array([10, 15, 20, 24, 31])

#where(condition ,true,false)
result=np.where(arr%5==0,"Multiple of 5","Not multiple of 5")

print(result)

print(np.extract(arr%2==0,arr))
