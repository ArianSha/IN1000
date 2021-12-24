#dette programmet printer en liste som har 4 int elementer, der bare forste og tredje element blir printet
#ny liste blir laget hvor bruker legger inn 4 navn i listen, if sjekk gjort om navnet mitt er i listen
#Summen og produktet av alle tallene i den forste listen blir lagt i en liste sammen
#Denne listen blir lagt i ny liste sammen med tall forste tall listen, så printet
#2 siste elementer fra listen blir fjernet saa printet paa nytt

import math

liste = [1,4,7]
liste.append(3)
#forste og tredje element blir printet
print(liste[0], liste[2])

navn = []
print('Oppgi fire navn: ') 
#for lokken kjorer 4 ganger, 4 navn lagt i liste "navn"
for x in range(4): 
    navnInput = input()
    navn.append(navnInput.lower())

#mitt navn er i listen
if 'arian' in navn:
    print('DU husket meg!')
#mitt navn er ikke i listen
else:
    print('Glemte du meg?')

sum = sum(liste)
#bruker bibliotek math, tall i 'liste' blir ganget sammen 
produkt = (math.prod(liste))
liste2 = []
#produkt og sum blir lagt inn i liste2 
liste2.extend([sum,produkt])

listeMerge = liste2 + liste
print(listeMerge)
#siste element i listen blir fjernet to ganger
del listeMerge[-1]
del listeMerge[-1]
print(listeMerge)