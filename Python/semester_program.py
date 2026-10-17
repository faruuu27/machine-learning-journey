def main():
    cgpa=float(input("Enter your cgpa: "))
    semester=int(input("Enter your semester: "))
    IntershipEligibility(cgpa,semester)
    

def IntershipEligibility(cgpa,semester):
    if cgpa<7.0:
        print("Not elgible: CGPA must be 7.0 or higher")
    else:
        if 1<=semester<=4:
            print("Eligible: Assigned to the Foundational Training track")
        elif 5<=semester<=8:
            print("Eligible:  Assigned to the Core Project track")
        else:
            print("Invalid Semester Entered")

main()