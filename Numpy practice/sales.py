import numpy as np
np.set_printoptions(precision=3)
# Rows = days, Columns = [ProductA, ProductB, ProductC] sales
sales = np.array([
    [100, 200, 150],
    [120, 210, 160],
    [90,  180, 140],
    [110, 220, 155]
])

print(sales)
print("Total sales per product: ", sales.sum(axis=0))
print("average sales per day: ", np.mean(sales,axis=1))

print("Best selling product : ", np.argmax(sales.sum(axis=0)))

print("Highest single day sale: " ,sales.max())