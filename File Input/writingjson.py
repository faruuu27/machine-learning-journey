import json

def main():

    students={
        "name":"farhan",
        "age": 22
    }

    with open("students4.json","w") as file:
        json.dump(students,file,indent=4)

main()
