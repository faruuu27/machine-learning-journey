import numpy as np


arr=np.array([1,2,3,np.nan,5])

print(np.mean(arr))
print(np.nanmean(arr))