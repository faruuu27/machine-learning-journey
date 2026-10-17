import json
def main():

    with open("employes.json",'r') as file:
        data=json.load(file)

    data['skills'][1]="javacript"

    with open("employes.json",'w') as file:
        json.dump(data,file,indent=4)

main()