# henter klassen person fra filen egenOppgave
from egenOppgave import person

#alt blir kjort i funksjonen hovedProgram
def hovedprogram():
    #objektet sitt parametere for konstruktoren blir bestemt fra input
    navn = input('skriv inn navn: ')
    alder = int(input('skriv inn alder: '))
    kevin = person(navn, alder)

    print('skriv inn din hobby, skriv \"avslutt\" nar du ikke vil legge til flere hobbyer ')
    # input blir lagt som hobby i liste helt til bruker skriver inn 'avslutt'
    while (hobby := input('')) != 'avslutt':
        kevin.leggTilHobby(hobby)
    #kaller paa metoden skrivUt
    kevin.SkrivUt()

hovedprogram()