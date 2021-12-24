from regneklynge import Regneklynge
from node import Node

class Datasenter:
    def __init__(self):
        self._regneklynger = {}

    def lesRegneklynge(self, fil):
        filNavn = fil 
        with open(fil) as fil:
            data = fil.read()
            listeData = data.split()
        nodeKapasitet = listeData.pop(0)

        nyRegneklynge = Regneklynge(nodeKapasitet)

        while 0 < len(listeData):
            antallNoder = listeData[0] 
            listeData.remove(antallNoder)
            
            minnePerNode = listeData[0] 
            listeData.remove(minnePerNode)
            
            antallProssesorPerNode = listeData[0] 
            listeData.remove(antallProssesorPerNode)

            for i in range(int(antallNoder)):
                NyNode = Node(minnePerNode, antallProssesorPerNode)
                nyRegneklynge.plasserNodeIRack(NyNode)
        
        self._regneklynger[filNavn] = nyRegneklynge
    
    def infoOmRegneklynge(self, soktRegneklynge):
        if soktRegneklynge in self._regneklynger:
            funnetRegneklynge = self._regneklynger[soktRegneklynge] 
            print(F'Regneklyngen {soktRegneklynge}: \nRack: {funnetRegneklynge.antallRacks()}.')
            print(F'Prosessorer: {funnetRegneklynge.antProssesorer()}. \n')
        else:
            print('Regneklyngen du har sokt finnes ikke')

    def utskriftAlt(self):
        for k, v in self._regneklynger.items():
            print(F'Regneklyngen {k}: \nRack: {v.antallRacks()}.')
            print(F'Prosessorer: {v.antProssesorer()}.')
            print(F'Antall noder med minst 32 GB: {v.noderMedNokMinne(32)}.')
            print(F'Antall noder med minst 64 GB: {v.noderMedNokMinne(64)}.')
            print(F'Antall noder med minst 128 GB: {v.noderMedNokMinne(128)}. \n')



