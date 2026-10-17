def main():

    a=[1,2,3]
    b=[4,5,6]
    dotProd=0
    for x in a:
        for y in b:
            temp=x*y
            dotProd+=temp
            break
        

    print(dotProd)

main()

