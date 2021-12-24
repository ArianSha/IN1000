def intro():
    navn = input("hei hva heter du? ")
    bosted = input("hvor kommer du fra? ")
    print("Hei " + navn + " du kommer fra " + bosted)
    print("")

for x in range(3):
    intro()
