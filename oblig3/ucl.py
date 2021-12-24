#Lag en fotballquiz om UEFA champions league, der du bruker mengder i quizen
#brukeren maa bare faa en riktig for aa faa poeng

#Fasit blir lagret i 3 ulike mengder, en for hvert sporsmaal
UclTopscorere = {'ronaldo', 'messi','lewandowski', 'benzema'}
UclSpillerMedFlestAssist = {'ronaldo', 'messi','di maria', 'giggs'}
LagMedFlestUcl = {'real madrid', 'milan','liverpool', 'bayern'}
poeng = 0

#Spiller maa bare vite en spiller av 4 mulige korrekte for a faa poeng
svar1 = input('Nevn en spiller som er i top 4 for flest maal i UEFA Champions League? ').lower()
if (svar1 in UclTopscorere):
    poeng+=1 

#Spiller maa bare vite en spiller av 4 mulige korrekte for a faa poeng
svar2 = input('Nevn en spiller som er i top 4 for flest assist i UEFA Champions League? ').lower()
if (svar2 in UclSpillerMedFlestAssist):
    poeng+=1 

#Spiller maa bare vite et lag av 4 mulige korrekte for a faa poeng
svar3 = input('Nevn et lag som er i top 4 for flest titler i UEFA Champions League? ').lower()
if (svar3 in LagMedFlestUcl):
    poeng+=1 

#Oppsumering av quiz
print(f'Quizen er ferding! Du fikk totalt {poeng} poeng')