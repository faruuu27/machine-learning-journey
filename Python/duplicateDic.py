from collections import Counter
def main():
    data = {"Farhan": 90, "Aania": 95, "George": 90, "Sarah": 95, "Alex": 82}

    value_count=Counter(data.values())

    duplicates={val:count for val,count in value_count.items() if count >1}

    print(duplicates)

main()