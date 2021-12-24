#Oppgavetekst: 
#skriv et monthy python program med bruk av liste, ene døren er ferrari og de andre er geit
import random
premier = ['ferrari', 'geit', 'geit']
randomPremierPlasering = random.shuffle(premier)
riktigDor = randomPremierPlasering.index('ferrari')

valg1 = input("Hei Spiller! Bak en av disse dorene ligger det en ferrari, velger du dor 1, 2 eller 3?")
# DorBakValg1 = premier.index(valg1-1)
valg1 = input("Hei Spiller! Bak en av disse dorene ligger det en ferrari, velger du dor 1, 2 eller 3?")
if valg1-1 == riktigDor:
    dorerEttervalg = 

    NyValg = input('B')
