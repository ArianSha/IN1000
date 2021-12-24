#dette programmet inneholder matvarer, der bruker kan legge til 2 varer og dens pris

#matvarer og pris blir lagret i ordbok "varer"
varer={"melk":14.90, "brød":24.90, "yogurt":12.90, "pizza":39.90}
print (varer)

#prossedyren legger til vare og verdi
def legge_til_vare():
    vare = input("legg til en vare: ").lower()
    verdi = input("legg til en verdi for varen:")
    varer[vare]=verdi

#prossedyren blir kjort 2 ganger
for x in range (2):
    legge_til_vare()
    
print(varer)