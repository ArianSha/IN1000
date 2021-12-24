def addisjon(tall1,tall2):
    return tall1 + tall2
def addisjonSjekk():
    assert addisjon(10,5) == 15, "funksjon er feil"
    assert addisjon(-2,-2) == -4, "funksjon er feil"
    assert addisjon(-6,2) == -4, "funksjon er feil"

def subtraksjon(tall1,tall2):
    return tall1 - tall2
def subtraksjonSjekk():
    assert subtraksjon(10,5) == 5, "funksjon er feil"
    assert subtraksjon(-5,-2) == -3, "funksjon er feil"
    assert subtraksjon(-6,3) == -9, "funksjon er feil"

def divisjon(tall1,tall2):
    return tall1/tall2
def divisjonSjekk():
    assert divisjon(10,5) == 2, "funksjon er feil"
    assert divisjon(-2,-2) == 1, "funksjon er feil"
    assert divisjon(-6,2) == -3, "funksjon er feil"


print(divisjon(3,4))

def tommerTilCm(antallTommer):
    assert antallTommer > 0
    cm = antallTommer * 2.54
    print(cm)

tommerTilCm(3)

def skrivBeregninger():
    InputTall1 = int(input('Oppgi tall 1: '))
    InputTall2 = int(input('Oppgi tall 2: '))

    print(f'Summen for addering: {addisjon(InputTall1,InputTall2)}')
    print(f'Summen for substraksjon: {subtraksjon(InputTall1,InputTall2)}')
    print(f'Summen for divisjon: {divisjon(InputTall1,InputTall2)}')

    InputTall3 = int(input('Oppgi et nytt tall: '))
    tommerTilCm(InputTall3)

if __name__ == '__main__':
    addisjonSjekk()
    subtraksjonSjekk()
    divisjonSjekk()
    skrivBeregninger()
