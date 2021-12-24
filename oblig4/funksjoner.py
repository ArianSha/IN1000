#Dette programmet har to prossedyrer med to ulike parametere.
#Den forste prossedyren tar i mot to tall og returnerer verdien av summen tallene.
#Den andre prossedyren tar i mot en setning og en bokstav, og sjekker forrekomster bokstaven har i setningen

def adder(tall1,tall2):
    return tall1+tall2
#Prossedyren adder blir kallt 2 ganger med bestemte tall
print (f'summen av 3 + 3 er {adder(3,3)}')
print (f'summen av 21 + 48 er {adder(21,48)}')

def tellForekomst(minTekst,minBokstav):
    bokstavIStreng=0

    #Sjekker forst om bokstav er i setningen, hvis den er i setning vil den begynne aa telle
    if minBokstav not in minTekst:
        print('bokstaven er ikke i strengen')
    else:
        for i in minTekst:
            if i == minBokstav:
                bokstavIStreng+=1
        print(f'bokstaven {minBokstav} har {bokstavIStreng} forekomster i strengen')

#Parametere til prossedyren tellForekomst blir definert her via bruker input 
x = (input('Skriv inn en setning '))
y = (input('skriv in en bokstav '))

tellForekomst(x,y)