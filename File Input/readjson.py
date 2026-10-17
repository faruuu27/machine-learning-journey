import json

def main():
    with open("students3.json") as file:
        data=json.load(file)  ##json.load converts JSON into python dictionary

    print(data)
    print(data['name'])

main()