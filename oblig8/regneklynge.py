
from rack import Rack 

# konstruktoeren lagger en regneklynge med 2 attributter,
# en liste med racks og maks antall noder i hver rack
class Regneklynge:
    def __init__(self, nodeKapasitet):
        self._racks = []
        self._nodeKapasitet = nodeKapasitet

    # metoden plasserer node gitt i parameter i en rack
    def plasserNodeIRack(self, node):
    # hvis det ikke finnes rack blir det skapt en ny rack, som node blir lagt inn
        if self._racks:
            # sjekker om noen racks har plass, 
            # vis den finner en rack med plass blir node lagt i og metoden stopper
            # hvis den ikke finner ledig rack blir ny rack skapt
            for rack in self._racks:
                if int(self._nodeKapasitet) > int(rack.antNoder()):
                    rack.leggInnNode(node)
                    return
            nyRack = Rack()
            nyRack.leggInnNode(node)
            self._racks.append(nyRack)
        else:
            nyRack = Rack()
            nyRack.leggInnNode(node)
            self._racks.append(nyRack)

    # metoden viser total antall prosessor i regneklybge
    def antProssesorer(self):
        antPros = 0
        for rack in self._racks:
            antPros += rack.sumPros()
        return antPros
    
    # metoden sjekker antall noder i regneklynge som har mer eller lik minne som blir gitt i parameter
    def noderMedNokMinne(self, paakrevdMinne):
        antNoderForBruk = 0
        for rack in self._racks:
            for node in rack._noder:
                if int(node._minne) >= paakrevdMinne:
                    antNoderForBruk += 1
        return antNoderForBruk
    
    
    # metoden returnerer antall racks i regneklynge
    def antallRacks(self):
        return len(self._racks)
