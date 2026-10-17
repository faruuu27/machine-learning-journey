import csv

def main():

    name=input("enter your name: ")

    school=input("enter your school: ")

    with open("student2.csv",'w',newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["name","school"])
        writer.writeheader()
        writer.writerow({"name":name,"school":school})

main()