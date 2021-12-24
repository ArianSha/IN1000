#dette programmet tar inn 2 fodselsdager og kalkulerer hvilket fodselsdag kommer forst

#denne funksjonen sikrer at brukeren skriver inn tall og ikke tekst
def inputSjekk(melding):
  while True:
    try:
        #Her vil den teste om input fra bruker kan konverteres til int
       brukerInput = int(input(melding))
    except ValueError:
        #hvis den faar 'valueError' kan den ikke konvertere til int, bruker faar feilmelding
       print("Ikke et heltall! Prov igjen")
       continue
    else:
        #hvis programmet kan bli konvertert til int vil den returnere input verdi
        return brukerInput

#Bruker blir bedt om aa skrive inn dato for egen bursdag
#Bruker skriver forst dag og saa maaned, begge to blir lagret i sin egen variabel
dag1 = inputSjekk('Hvilken dag i maaneden er du fodt i? (svar 1-31) ')
maaned1 = inputSjekk('Hvilken maaned er du fodt i? (svar 1-12)')

#Bruker blir bedt om aa skrive inn dato for egen bursdag
#Bruker skriver forst dag og saa maaned, begge to blir lagret i sin egen variabel
dag2 = inputSjekk('Hvilken dag i maaneden er bestevennen din fodt i? (svar 1-31) ')
maaned2 = inputSjekk('Hvilken maaned er bestevennen din fodt i? (svar 1-12) ')

#Denne if sjekken sjekker hvilken dato kommer forst
if maaned1<maaned2:
    print('Riktig rekkefolge!')
elif maaned1>maaned2:
    print('Feil rekkefolge!')
else:
    if dag1<dag2:
        print('Riktig rekkefolge!')
    elif dag1>dag2:
        print('Feil rekkefolge')
    else:
        print('Samme dato!')

