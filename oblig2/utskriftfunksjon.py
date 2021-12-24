#Dette programmet har en prossedyre som tar inn bosted og navn fra bruker, og skriver til slutt en hilsen. 

#kommandoene blir lagret inni Prossedyren 'introdukjson'
def introduksjon():
    #Bruker skriver inn navn, blir lagret i variabel navn
    navn = input("Skriv inn navn ")
    #Bruker skriver inn bosted, blir lagret i variabel navn
    bosted = input("Hvor kommer du fra? ")
    #program sender hilsen ut ifra variabel navn og variabel bosted
    print(f'Hei, {navn}! Du er fra {bosted}.')

#Denne for lokken faar prossedyren til aa kjore 3 ganger
for x in range(3):
    introduksjon()
