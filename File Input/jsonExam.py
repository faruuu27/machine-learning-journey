from json import load
def main():
    with open("students3.json","r+") as file:
        py_dict=load(file)

        py_dict['course']="Artifical Intelligence"
    
            
            


main()

