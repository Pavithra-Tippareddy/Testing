class delivery:
    item = ""
    name = ""
    address = ""


def addnew():
    customer = input("Enter the customer name?\n")
    place = input("Enter location\n")
    stuff = input("What is the thing?\n")

    packet = delivery()
    packet.name = customer
    packet.address = place
    packet.item = stuff
    return packet


def main():
    round = [ ]
    total = int(input("How many packages?:"))
    for i in range(0, total):
        deliver = addnew()
        round.append(deliver)
    print("Drop-off places:")

    for i in range(0, total):
        print(round[i].name + ":" + round[i].address + ":" + round[i].item)


if __name__ ==  "__main__":
        main()









