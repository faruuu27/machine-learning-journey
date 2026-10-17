import numpy as np

mat = np.array([[3, 2], [3, 4]])
rows,cols=np.where(mat>2)

print(rows,cols)
print(list(zip(rows,cols)))