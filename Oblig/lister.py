import numpy
ucl = [13,6,4]

ucl.append(int(input("legg til et tall: ")))
print("her er det første og tredje tallet i listen: ", ucl[0], ucl[2])

liste=[]
def legg_til_navn():
    navn = input("oppgi et navn: ")
    navn = navn.lower()
    liste.append(navn)

    
for x in range(4):
    legg_til_navn()

if "arian" in liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")  

ucl_ganget = 1
ucl_plusset = 0
for tall in ucl:
    ucl_ganget = ucl_ganget*tall
    ucl_plusset = ucl_plusset+tall

ucl_endret = [ucl_ganget, ucl_plusset]

ucl_comb = (ucl + ucl_endret)
print("Her er den originale listen, + summen av listen og listen ganget sammen" , ucl_comb)

ucl_comb = ucl[:len(ucl_comb)-2]
print("Her er listen - de to siste tallene", ucl_comb)


