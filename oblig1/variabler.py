#dette programmet tar inn navn fra brukeren, og gir en hilsen
#dette programmet gir deretter 2 input der bruker skal taste in tall
#Deretter blir differansen av det første tallet og andre tallet printet
#Bruker skal til slutt oppgi et navn til, de to navnene nevnt skal printes sammen i en ny variabel

navn = input('Hva heter du? ')
print(f'Hei {navn}')

#gjor om input til int for aa kunne regne med
tall1 = int(input('tast inn et tall: '))
tall2 = int(input('tast inn et tall til: '))
print(tall1)
print(tall2)
diff = tall1-tall2
#bruker f string for aa lett kunne printe tekst og tall sammen
print(f'Differanse {diff}')

navn2 = input('Vennligst oppgi et nytt navn: ')
sammen = navn + navn2
#Begge navnene blir lagret i variabel sammen, med "og" mellom dem
sammen = f'{navn} og {navn2}'
print(sammen)