import time
import sys
import numpy as np

def main():
    l=range(1000)
    print(sys.getsizeof(5)*len(l))

    array=np.arange(1000)
    print(array.size*array.itemsize)

main()
