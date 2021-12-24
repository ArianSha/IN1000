# Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
# og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
# instansvariabel hobbyer som en tom liste . Skriv en metode leggTilHobby som tar
# imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
# skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
# Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
# alder kaller på metoden skrivHobbyer.
# Lag deretter et testprogram for klassen Person der du lar brukeren skrive inn navn og
# alder, og oppretter et Person-objekt med informasjonen du får. Deretter skal brukeren
# ved hjelp av en løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger
# ønsker å oppgi hobbyer skal informasjon om brukeren skrives ut.

class person:
    # definerer konstruktoren
    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder
        # definerer utsagnsvariabelen hobber som en liste
        self.hobbyer = []

    def leggTilHobby(self, hobby):
        self.hobbyer.append(hobby)
    
    #skriver ut elementene i listen hobbyer
    def skrivHobbyer(self):
        # hvert element blir pakket ut fra listen og printet
        print('Hobbyer:')
        print(*self.hobbyer, sep ='\n')
    
    # skriver ut navn, alder og kaller paa metode skrivHobbyer
    def SkrivUt(self):
        print(f'Navn: {self.navn}, alder: {self.alder}.')
        self.skrivHobbyer()