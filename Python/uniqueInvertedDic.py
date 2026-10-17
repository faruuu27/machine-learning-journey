def main():
    grades = {"Farhan": 90, "Aania": 95, "George": 90, "Sarah": 95}

    inverted={value : key for key,value in grades.items()}

    print(inverted)

main()