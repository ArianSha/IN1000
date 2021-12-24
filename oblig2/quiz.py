resultat = []

def quiz(sporsmaal, fasit, sisteSporsmaal):
    svar = (input(sporsmaal)).lower()

    if not sisteSporsmaal:
        if svar == fasit:
            resultat.append(True)
            print (f'riktig! Poengsum = {resultat.count(True)}')

        else:
            resultat.append(False)
            print ('Feil svar')

    #riktig svar og siste sporsmaal 
    else:
        if svar == fasit:
            resultat.append(True)
            print ('Riktig svar!')
            print (f'Quizen er ferdig. Du fikk totalt {resultat.count(True)} poeng! Her er resultatet:')
            #Bygger en ny liste der hvert element og dens plass i array 'resultat' printes
            print ([list((i+1, resultat[i])) for i in range(len(resultat))])

        #feil svar og siste sporsmaal 
        else:
            resultat.append(False)
            print ('Feil svar')
            print (f'Quizen er ferdig. Du fikk totalt {resultat.count(True)} poeng! Her er resultatet:')

            print ([(i+1, spoersmaal) for i, spoersmaal in enumerate(resultat)])


if __name__ == '__main__':
    mal = [
        ('Hvilket fotball lag vant Champions League i 2017? ','real madrid'),
        ('Hvilken big tech bedrift la ut den ikoniske reklamen 1984 som var basert paa George Orwell sin novelle Nineteen Eighy-four? ','apple'),
        ('Hvem er Tesla sin CEO? ','elon musk'),
        ('Hvilken krypto valutta blir ofte kalt en fase en fremtidig fase 3 mynt? ','cardano')
    ]

    for i, (spm, fasit) in enumerate(mal):
        siste_spm = i == len(mal) - 1
        quiz(spm, fasit, siste_spm)