#dette programmet skriver ut Navnet til beboere, og skriver ut matplan til beboer som er sokt etter

#matplanen er lagret i ordbok
mat = {'magnus':{'frokost': 'omelett', 'lunsj': 'pizza', 'middag': 'pasta'}, 
'nora':{'frokost': 'havregryn', 'lunsj': 'suppe', 'middag': 'kylling'},
'stian':{'frokost': 'omelett', 'lunsj': 'kebab', 'middag': 'biff'},  
}

def sykehjemPlan():
    print (f'Navnene paa alle i sykehjemmet: {mat.keys()}')
    beboerInput = input('Skriv inn navn til en beboer for beboer sin matplan : ').lower()

    try:
        #hvis beboer er gylid kan matplanen bli printet 
        print(f'Beboeren sin matplan er: {mat[beboerInput]}') 
    except KeyError:
        #hvis beboer ikke er gylid er det keyerror, bruker har tastet feil 
        print('Beboeren du har skrevet inn er ikke registret')

sykehjemPlan()

#Svar paa oppgave 4: deloppgave 3 
#a: jeg hadde valgt ordbok for brukernavn for alle in1000 studenter
    #dette er for at annet brukerinformasjon skal vaere tilkoblet til brukernavnet, 
    #som f.eks at en bruker har glemt passord og nytt passord blir sendt til mail
#b: Jeg hadde brukt ordbok slik at brukernavn blir assigna deres poeng
#c: Jeg hadde brukt Array siden mengde tilater ikke duplikater
#d: Jeg hadde brukt ordbok slik at spesifike gjester har en egen matplan 
    #Hvis det var planlagt aa fjenre allergisk mat for alle sammen, hadde jeg valgt mengde siden rekkefolge og forrekomster ikke er viktig 