import csv
def main():

    with open("marks.csv",'r') as file:
        reader=csv.DictReader(file)
        print(reader)
        rows=list(reader)
        fieldnames=reader.fieldnames

    for row in rows:
        if row['name']=="Diya":
            row['math']=98
    
    with open("marks.csv",'w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

main()