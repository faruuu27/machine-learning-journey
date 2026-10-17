import numpy as np
np.set_printoptions(suppress=True,precision=3)  ## this will print values normal instead of scientfic notaion

house_features=np.array([[1500,3,300000],
                         [2500,4,400000],
                         [1200,2,250000]])

mean=house_features.mean(axis=0) ## get  each column mean

std=house_features.std(axis=0) ##get standard deviation of each column
print(mean)

print("after z score normalization: ")
z_normalization = (house_features - mean) / std
print(z_normalization)


