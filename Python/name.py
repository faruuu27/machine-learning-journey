def main():
    name=input("Enter your name: ").strip().title()
    print(name)
    status= True if name.startswith("A") else False
    print(status)
main()
