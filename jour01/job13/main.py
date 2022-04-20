# Créez un programme qui demande 5 fois à l’utilisateur de renseigner un nombre entier.
# Stockez ces nombres entiers dans une liste puis triez-les par ordre croissant avant de
# les afficher, dans l’ordre, dans le terminal.

tab = [] # tableau resultat
# i = 5 # nb tour
for i in range(1,6):
    print('Veuillez renseigner un nombre entier, juste comme ça')
    x = input()
    tab.append(x)

print(tab)
tab.sort()

print(tab)