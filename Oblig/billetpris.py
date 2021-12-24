def pris():
    alder = input("hva er alderen din? ")
    
    if(alder.isdigit()):
         alder = float(alder)
         billetpris=0
         if alder <= 17:
             billetpris = 30 
         elif 63 > alder > 17:
             billetpris = 50
         else:
             billetpris = 35
    
         print("prisen for billeten din blir:" , billetpris , "kroner")
         print("")
    else:
        print("Du må taste inn et tall!")
        print("")

for x in range(4):
    pris()

#jeg har lagt til float på input, slik at desimal regnes med og
#hvis noen skriver tekst har jeg svart at brukeren må skrive et tall