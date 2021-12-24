#definerer klassen Motorsykkel
class Motorsykkel:
    #definerer konstruktoeren til klassen
    # tar imot 3 parametere: merke, registrering, kilometer
    def __init__(self, merke, registrering, kilometer):
        self.merke = merke
        self.registrering = registrering
        self.kilometer = kilometer

    # oeker kilometerstand med verdien i parameteren
    def kjor(self, kilometer):
        self.kilometer += kilometer
        # print(f'Motorsykkelen har {self.kilometer} ')
   
    # returnerer kilometerstanden
    def hentKilometerstand(self):
        return self.kilometer
    #   printer motorsykkelen sitt merke, registreringsnummer og kilometerstand
    def skrivUt(self):
        print(f'Motorsykkelen sitt merke: {self.merke} ')
        print(f'Motorsykkelen sitt registreringsnummer: {self.registrering} ')
        print(f'Motorsykkelen sitt merke: {self.kilometer} ')

    

