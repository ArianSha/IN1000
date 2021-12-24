#definerer klassen hund
class hund:
    # definerer konstruktoren med 3 parametere: alder, vekt og metthet
    def __init__(self, alder, vekt, metthet):
        self.alder = alder
        self.vekt = vekt
        self.metthet = metthet
    
    # returnerer vekten
    def utskriftVekt(self):
        return self.vekt
    
    # returnerer alderern
    def utskriftAlder(self):
        return self.alder
    
    # Hunden 'springer' og mistter metthet med 1
    # hunden mister da vekt hvis mettet er lavere enn 5
    #Returnerer til slutt hunden sin vekt
    def spring(self):
        self.metthet += -1
        if(self.metthet < 5):
            self.vekt += -1
        return self.vekt

    # Hunden "spiser"
    # Tar imot parameteter som oker metthet
    # Hvis metthet er da hoeyere enn 7 okes vekt med 1
    # Returnerer til slutt hunden sin vekt
    def spis(self, metthetInput):
        self.metthet += metthetInput
        if (self.metthet > 7):
            self.vekt += 1
        return self.vekt