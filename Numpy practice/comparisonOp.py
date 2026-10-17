import numpy as np

score= np.array([87,67,90,55,81,97,100])
score[score<60]=0
print(score)