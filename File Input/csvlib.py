import csv

def main():
    students=[]
    with open("students.csv") as file:
        reader=csv.reader(file)
        for name,school in reader:
            students.append({"name":name , "school":school})

    for student in sorted(students, key=lambda student: student['name']):
        print(f"{student['name']} is from {student['school']}")

main()