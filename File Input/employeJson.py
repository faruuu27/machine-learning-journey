import json

def main():

    with open("employes.json") as file:
        data=json.load(file)

    print(data["address"]["city"])
    print(data["skills"][2])

main()