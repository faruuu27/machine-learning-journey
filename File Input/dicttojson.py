import json

def main():
    students={
        "name":"farhan",
        "age": 22
    }

    text=json.dumps(students)
    
    print(text)

main()