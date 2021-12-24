#dette programmet sjekker alderen til brukeren, og regner ut billeprisen

#alder er et parameter i prosedyren, brukerens input svar blir tolket som alder
def billetSjekk(alder):
    if alder <= 17:
        billettpris = 30
        print(f'Billetprisen er {billettpris} ')
    elif alder > 17 and alder < 63:
        billettpris = 50
        print(f'Billetprisen er {billettpris} ')
    else:
        billettpris = 35
        print(f'Billetprisen er {billettpris} ')

billetpris = 0
billetSjekk(int(input('Skriv inn alder til kjoperen av billeten: ')))

#Programmet kjorer feilfritt med ingen problemer 