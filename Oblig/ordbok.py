varer={"melk":14.90, "brød":24.90, "yogurt":12.90, "pizza":39.90}

def legge_til_vare():
    vare = input("legg til en vare: ").lower()
    verdi = input("legg til en verdi for varen:")
    varer[vare]=verdi

for x in range (2):
    legge_til_vare()
    
print(varer)