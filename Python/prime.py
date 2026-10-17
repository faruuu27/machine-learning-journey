def main():
    num=int(input("enter your number: "))
    print(checkPrime(num))

def checkPrime(n):
    
    if n<2:
        return "not prime"
    else:
        for i in range(2, (n//2)+1):
            if n%i==0:
                return "not prime"
                break
        else:
            return "prime"






main()