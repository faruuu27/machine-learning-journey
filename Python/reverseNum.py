def main():
    num=int(input("Enter your number: "))
    print(reverse(num))

def reverse(n):
    temp=str(n)
    return int(temp[::-1])

main()