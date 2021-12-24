# henter klassen Motorsykkel fra filen motorsykkel
from motorsykkel import Motorsykkel

#alt blir kjort i funksjonen hovedProgram
def hovedprogram():
    # objektet motor1 blir definert med gitte parametere
    motor1 = Motorsykkel('bmw','2018', 3)
    # kaller paa metoden skrivUt for objektet 'moto1'
    motor1.skrivUt()

    # objektet motor2 blir definert med gitte parametere
    motor2 = Motorsykkel('harley','2007', 34)
    # kaller paa metoden skrivUt for objektet 'motor2'
    motor2.skrivUt()

    # objektet motor3 blir definert med gitte parametere
    motor3 = Motorsykkel('honda','2013', 15)
    # oeker kilometerstanden med 10 for objektet "motor3"
    motor3.kjor(10)
    # kaller paa metoden hentKilometerstand for objektet 'motor2'
    motor3.hentKilometerstand()
    # kaller paa metoden skrivUt for objektet 'motor3'
    motor3.skrivUt()

hovedprogram()