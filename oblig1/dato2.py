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

#bruker oppgir to ulike datoer, deretter blir input omgjort til int for aa bli regnet med. 
dato1 = int(inputSjekk('Skriv datoen til din bursdag? (svar i heltall der fyrste er dag og andre er maaned f.eks ''128'' = 8 desember) '))
dato2 = int(inputSjekk('Hvilken dag i maaneded er bestevennen din fodt i? (svar i heltall der fyrste er dag og andre er maaned f.eks ''128'' = 8 desember) '))

#denne if sjekken sjekker hvilken dato kommer forst, og printer
if dato1<dato2:
    print('Riktig rekkefolge!')
elif dato1>dato2:
    print('Feil rekkefolge!')
else:
    print('Samme dato!')
