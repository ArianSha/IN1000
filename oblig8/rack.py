
from node import Node

# konstruktoeren lager Racks med et attributt som er en liste med noder 
class Rack:
    def __init__(self) -> None:
         self._noder = []
    
    # metoden legger node i rack
    def leggInnNode(self, node):
        self._noder.append(node)
    
    # metoden teller antar noder i rack 
    def antNoder(self):
        return len(self._noder)
    
    # metoden teller antar prosessorer i rack 
    def sumPros(self):
        sum = 0
        for node in self._noder:
            sum += int(node._antPros)
        return sum
    
    # metoden sjekker antall noder i rack som har mer eller lik minne som blir gitt i parameter
    def noderMedNokMinne(self, paakrevdMinne):
        antNoderForbruk = 0
        for node in self._noder:
            if int(node._minne) >= int(paakrevdMinne):
                antNoderForbruk += 1
        return antNoderForbruk