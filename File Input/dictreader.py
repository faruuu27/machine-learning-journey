import csv

def main():
    students=[]
    with open("students.csv") as file:
        reader= csv.DictReader(file)
        for row in reader:
            students.append({"name":row["name"], 
                             "school": row["school"],
                             "age":row['age']})

    for student in sorted(students, key=lambda student: student['school']):
        print(f"{student['name']} is from {student['school']} and age is {student['age']}")

main()