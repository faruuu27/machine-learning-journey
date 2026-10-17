
def main():
    count=0
    sum=0

    while(True):
        num=int(input("Enter a number: "))
        if(num==-1):
            break
        elif(num%2==0):
            count+=1
        else:
            sum+=num
    print(f"total number of even number: {count}")
    print(f"sum of odd numbers: {sum}")
    
main()