def main():
    total_bill=float(input("enter the total food bill: "))
    tip_perc=int(input("enter the tip percentage: "))
    nmbr_of_ppl=int(input("enter the number of people: "))
    print(f"The total bill amount including the tip is : {TotalBill(total_bill,tip_perc)}")
    print(f"Each person owes {TotalBill(total_bill,tip_perc)/nmbr_of_ppl}")
def TotalBill(bill,tip):
    return bill+(bill*(tip/100))

main()