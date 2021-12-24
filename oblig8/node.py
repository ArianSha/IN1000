
class Node:
# konstruktoeren lager Noder med 2 attributter: minne, og antall prosessor 
    def __init__(self, minne, antPros) -> None:
        self._minne = minne
        self._antPros = antPros
    
# metoden returnerer antall prosessor for en node
    def antPros(self):
        return self._antPros
    
# metoden sjekker om en node har mer eller lik minne blir gitt i parameter
    def nokMinne(self, krevdMinne):
        if self._minne >= krevdMinne:
            return True
        else:
            return False