import csv

def main():

    name=input("enter your name: ")
    school=input("enter your school: ")

    with open("student2.csv",'a') as file:
        writer=csv.DictWriter(file,fieldnames=["name","school"])
        writer.writerow({"name":name,"school":school})

main()