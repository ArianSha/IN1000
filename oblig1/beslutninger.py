#dette programmet spor bruker om brusvalg
#svaret blir kjort gjennom en if sjekk, og gir en tilbakemelding 

#Her brukes .lower for at input skal tolkes korrekt uavhengig av case
#dette hindrer og for aa skrive en mer avansert if sjekk
brusValg = input('Hvil du ha en brus? ').lower()

#input er lowercase, if bettingelser har bare tre alternativer
if brusValg == 'ja':
    print('Her har du en brus!')
elif brusValg == 'nei':
    print('Den er grei')
else:
    print('Det forstod jeg ikke helt')