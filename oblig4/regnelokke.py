def minsteTall(tall_liste):
    minste = tall_liste[0]

    for tall in tall_liste:
        if tall < minste:
            minste = tall

    return minste

def stoersteTall(tall_liste):
    stoerste = tall_liste[0]

    for tall in tall_liste:
        if tall > stoerste:
            stoerste = tall

    return stoerste

def sum(tall_liste):
    sum = 0
    for tall in tall_liste:
        sum += tall

    return sum

min_liste = []
min_sum = 0

while (inputBruker := int(input('Skriv inn et tall '))) != 0:
    min_liste.append(inputBruker)
    
MinsteTalliListe = min_liste[0]
StorsteTallListe = min_liste[0]



print(f'Summen av listen er {MinSum}')
print(f'Minste tallet i listen er {minsteTall(MinListe)}')

for x in MinListe:
    if MinsteTalliListe < x:
        MinsteTalliListe = x
        
print(f'Storste tallet i listen er {MinsteTalliListe}')