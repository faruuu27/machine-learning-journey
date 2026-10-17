def main():
    userInput=input("check palindrome: ").lower().replace(" ","").strip()
    print(checkPalindrome(userInput))

def checkPalindrome(str):
    reverse= str[::-1]
    return str==reverse
    
main()
