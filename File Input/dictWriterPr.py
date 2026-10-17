import csv
def main():

    name=input("enter your name: ")
    school=input("enter your school: ")

    with open("student2.csv",'a') as file:
        writer=csv.DictWriter(file,fieldnames=["Name","School"])
        writer.writerow({"Name":name,"School":school})

main()