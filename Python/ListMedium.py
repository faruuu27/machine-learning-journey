def main():
    inventory = ["laptop", "mouse", "keyboard", "monitor"]
    inventory.append("hdmi cable")
    indx=inventory.index("mouse")
    inventory.pop(indx)
    indx2=inventory.index("keyboard")
    inventory[indx2]="mechanical keyboard"
    print(inventory)



main()