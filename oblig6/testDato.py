#Henter klassen Dato fra filen dato
from dato import Dato

#alt blir kjort i funksjonen hovedProgram
def hovedProgram():
    dato1 = Dato(15,2,2002)
    print(dato1._nyttAar)

    # sjekker om dag er 15 eller 1 og gir melding
    if dato1._nyDag == 15:
        print('Loenningsdag!')
    elif dato1._nyDag == 1:
        print('Ny maaned, nye muligheter ')

    # lagrer return verdi fra metoden i variabel DatoUtskrift
    DatoUtskrift = dato1.datoEnkelUtskrift()
    print(DatoUtskrift)

    #kaller paa metode Dato2EtterDato1Sjekk
    dato1.Dato2EtterDato1Sjekk(3,2,2002)

hovedProgram()