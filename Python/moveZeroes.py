def main():
    lst=[1,0,4,2,0,0]

    non_zeroes=[n for n in lst if n!=0]

    zero_count=lst.count(0)

    result=non_zeroes+ [0]* zero_count

    print(result)

main()
