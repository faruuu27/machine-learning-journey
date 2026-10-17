import csv
def main():
    students=[]
    with open("students.csv",'r') as file:
        reader=csv.reader(file)
        next(reader)
        for row in reader:
            name=row[0]
            age=int(row[1])
            school=row[2]
            student={'name':name ,'age':age,'school':school}
            students.append(student)

    for student in sorted(students, key=lambda student:student['name']):
        print(student['name'])
main()
            