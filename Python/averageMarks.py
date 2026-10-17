def main():
    classroom = {
        "Farhan": [80, 85, 90],
        "Aania": [92, 95, 98],
        "George": [70, 65, 75]
    }
    student_name="jasna"

    print(f"{student_name} mark : {classroom.get(student_name,'not found')}")

    for student,marks in classroom.items():
        avg= sum(marks)/len(marks)
        print(f"{student} has an average score of {avg:.2f}")
    
main()