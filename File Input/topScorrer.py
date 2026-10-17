import csv
from tabulate import tabulate
def main():
    students=[]
    with open("marks.csv",'r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            student={
                "name": row['name'],
                "math": int(row['math']),
                "english": int(row["english"]),
                "science":int(row["science"])
            }
            students.append(student)

    print(tabulate(students, headers="keys", tablefmt="grid"))

main()


