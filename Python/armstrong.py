def main():
    num=int(input("enter your number: "))
    print(isArmstrong(num))

def isArmstrong(num):
    digits=len(str(num))
    total=0
    temp=num

    while temp>0:
        digit=temp%10
        total+= digit**digits
        temp//=10

    return True if num==total else False

main()