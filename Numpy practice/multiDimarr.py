import numpy as np

def main():

    array=np.array([[[1,2,3],[4,5,6],[7,8,9]],
                   [[1,2,3],[4,5,8],[7,8,9]]]
                   )

    print(array.ndim)
    print(array.shape)

    print(array[1,1,2])
    num= array[1,1,2]+array[0,0,0]  #8+1
    print(num)
    

main()

