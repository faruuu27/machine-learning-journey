from collections import defaultdict
def main():

    grades = {"Farhan": 90, "Aania": 95, "George": 90, "Sarah": 95}  #orginal dictionary

    inverted=defaultdict(list)

    for key,value in grades.items():

        inverted[value].append(key)

    print(inverted)

main()
    