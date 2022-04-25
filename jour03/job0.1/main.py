# Créer un programme qui lit le contenu du fichier “output.txt” et qui l’affiche dans le
# terminal.
def readString():
    file = open('output.txt', 'r') 
    print(file.read())
    file.close()

readString()