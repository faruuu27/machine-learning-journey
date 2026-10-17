import numpy as np

rng=np.random.default_rng()

print(np.random.uniform(low=-1,high=1,size=(3,2)))


print(rng.integers(low=1,high=101,size=(5,4)))

arr=np.array([1,2,3,4,5])
rng.shuffle(arr)
print(arr)

values=rng.choice(arr,size=3)

print(values)