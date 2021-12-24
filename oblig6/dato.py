# dette programmet inneholder en klasse Dato som har flere ulike metoder
# Konstruktoren tar imot 3 parametere: dag, maaned og aar

#definerer klassen Dato
class Dato: 
    maaneder = ['januar','februar','mars','mai','juni','juli','august','september','august','oktober','november','desember'  ]
    # definerer konstruktoeren med dag, maaned og aar som parametere
    def __init__ (self, nyDag, nyMaaned, nyttAar):
        self._nyDag = nyDag
        self._nyMaaned = nyMaaned
        self._nyttAar = nyttAar

    # returnerer aaret 
    def lesAar(self):
        return self._nyttAar
    
    #returnerer dato i en enkel utskrift
    def datoEnkelUtskrift(self):
        #maanedstring tilsvarer maaneden oppgit i tall, maanedstring er element i listen maaneder
        maanedString = Dato.maaneder[self._nyMaaned-1] 
        datoStreng = (f'Datoen er {self._nyDag}.{maanedString} {self._nyttAar}')
        return datoStreng
    
    # sjekker om datoen er en i januar, returnerer true hvis ja og false hvis nei
    def datoSjekk(self):
        if Dato.maaneder[self._nyMaaned - 1] == 'januar':
            return True
        else:
            return False
    
    # sjekker hvilken dato kommer forst
    def Dato2EtterDato1Sjekk(self, dag2, maaned2, aar2):
        if self._nyttAar < aar2:
            print('Nye datoen kommer etter fyrste dato')
        elif self._nyttAar > aar2:
            print('Nye datoen kommer foer fyrste dato')
        else:
            if self._nyMaaned<maaned2:
                print('Nye datoen kommer etter fyrste dato')
            elif self._nyMaaned>maaned2:
                print('Nye datoen kommer foer fyrste dato')
            else:
                if self._nyDag<dag2:
                    print('Nye datoen kommer etter fyrste dato')
                elif self._nyDag>dag2:
                    print('Nye datoen kommer foer fyrste dato')
                else:
                    print('Datoene er like.')
    
    