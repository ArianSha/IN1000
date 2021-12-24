#importerer klassen hund fra filen hund
from hund import hund

#alt blir kjort i funksjonen hovedProgram
def hovedProgram():
    # objektet hund1 blir definert med gitte parametere
    hund1 = hund(3,23,4)

    # kaller metoden spring for objektet hund1
    hund1.spring()
    print(f'Hundens vekt er: {hund1.vekt}')
    # kaller metoden spis for objektet hund1, med angitte parametere
    hund1.spis(2)
    print(f'Hundens vekt er: {hund1.vekt}')

    # kaller metoden spring for objektet hund1
    hund1.spring()
    print(f'Hundens vekt er: {hund1.vekt}')
    # kaller metoden spis for objektet hund1, med angitte parametere
    hund1.spis(7)
    print(f'Hundens vekt er: {hund1.vekt}')

hovedProgram()