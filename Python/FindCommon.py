def main():

    list1=[1,3,4,5,2,5]
    list2=[4,5,2,8,0,9]

    common=list(set(list1) & set(list2))

    print(common)

main()