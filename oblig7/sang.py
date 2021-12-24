class Sang:
    def __init__(self, artist, tittel):
        self._artist = artist 
        self._tittel = tittel
    
    def spill(self):
        print(f'Spiller naa {self._tittel}, av {self._artist} ')

    def sjekkArtist(self, navn):
        listeNavnBruker = navn.split()
        artistSplit = self._artist.split()

        if(any(i in listeNavnBruker for i in artistSplit)):
            return True
        else:
            return False

    def sjekkTittel(self, tittel):
        if self._tittel.lower() == tittel.lower():
            return True
        else:
            return False
    
    def sjekkArtistOgTittel(self, artist, tittel):
        artistBoolean = self.sjekkArtist(artist)
        tittelBoolean = self.sjekkTittel(tittel)

        if artistBoolean == True and tittelBoolean == True:
            return True
        else:
            return False

