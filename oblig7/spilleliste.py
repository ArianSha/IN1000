from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        #leser txt fil og lagrer det i linjer
        with open(filnavn) as fil:
            data = fil.read()
            listeData = data.splitlines()

        #spliter linje i to. for ; er tittel, etter ; er artist 
        for x in listeData:
            sang = (x.split(";",1))
            tittel = sang[0] 
            artist = sang[1] 
            self._sanger.append(Sang(artist,tittel))

    def leggTilSang(self, nySang): 
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        self._sanger.remove(sang)

    def spillSang(self, sang):
        sang.spill()

    def finnSang(self, tittel):
        for sang in self._sanger:
            if sang._tittel == tittel:
                return sang
        return None

    def spillAlle(self):
        for x in self._sanger:
            # print(x._artist, x._tittel)
            sang = Sang(x._artist, x._tittel)
            sang.spill()
    
    def hentArtistUtvalg(self, artistnavn):
        artistSangListe = []

        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn) == True:
                artistSangListe.append(sang)        
        return artistSangListe
