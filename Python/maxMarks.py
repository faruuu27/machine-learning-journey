def main():
    stats = {"Farhan": 88, "Aania": 95, "George": 72, "Sarah": 91}

    top_student=min(stats,key=stats.get)

    print(f"{top_student} : {stats[top_student]}")

main()
