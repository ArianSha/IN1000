def lagBrukernavn(fulltNavn):
    listeSplit = fulltNavn.split()
    forNavn = listeSplit[0]
    etterNavn = listeSplit[1]
    return f'{forNavn} {etterNavn[1]}'

def lagEpost(brukernavn, epostSuffix):
    epost = f'{brukernavn}@{epostSuffix}'
    return epost

def skrivUtEposter(ordbokBruker):
    ordbokBruker



if __name__ == '__main__':
    print(lagBrukernavn(input('Skriv inn ditt hele navn: ').lower()))

    skrivUtEposter({'olan': 'ifi.uio.no', 'karin':'student.matnat.uio.no'})
