# Créer un programme qui modélise un plateau de jeu, carré, de n x n cases. Placez sur ce
# plateau n dames de jeu d'échecs, de manière à ce qu’aucune dame ne puisse se
# “prendre”, quand cela est possible. La valeur de n est renseignée par l’utilisateur. Quand
# cela est possible, le programme devra afficher dans le terminal le plateau de jeu avec le
# caractère ‘O’ pour les cases vides et le caractère ‘X’ pour représenter les dames.

grid =[
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]




def echiquier(n, position):
    if(n == 0):
        return 1
    bool = True
    i = 0
    # print(position[i])
    # print('coucou')
    # if(position):
    #     grid[0][0] = 'x'
    #     position[i] = list(enumerate([x, y, z]))
    #     print(position)
    # x = colonne || need un compteur
    # y = rangée || need un compteur
    # z = positionnement d'une reine || need un compteur 
    # je passe les coordonnées de chaque reine en parametre de ma fonction
    # lorsque je compare les position je créer un décalage ou permutation pour
    # placer mes nouvelles reines par rapport aux anciennes
    # J'affiche grid


    for x in range(8):
        j = 0
        z = 0 # dames

        for y in range(8):
            # if(grid[x][y]) == 'x':
            print(position)
            if(position == 'x'):
                grid[x][y] = 'x'
                position = list(enumerate([x, y, z]))

                position = grid[x][y][z] 
                z +=1 
                print(position)
                break
            # if(position[i][[x][y]])
            j += 1
        i += 1


    i = 0
    for x in range(8):
        j = 0
        for y in range(8):
            if(position == grid[x][y]):
                if(i <= 6 or j <= 6): 
                    print('coucou')
                    grid[x][y] = 'x'
                else:
                    grid[x+2][y+2] = 'x'

    
            y += 1
        i += 1

    #         # if(grid[x][y] == 'x'):
    #         #     bool = False
    #         # elif(bool):
    #         #     grid[x][y] = 'x'
    #         # else:
    #         #     bool = False
    #         # i += 1
    
    echiquier(n-1, position)
    print(grid)



echiquier(8, 0)

    