# Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre de mots
# de chaque taille. A l’aide du module MatPlotLib, générer un histogramme représentant
# le pourcentage d’apparition de chaque taille de mot.

# algo qui detect des taille de mots différentes et qui les inseres dans un new tab
# ensuite a chaque fois qu'un len est detecté on fait un i++
# -> histogramme a partir de la


import re


file = open('data.txt', 'r')

x = re.findall("\S[A-z]+",  file.read())
print(x)
dic = {}
for word in x:
    #     i = 0

    #     for letter in x:
    #         if (char == letter):
    #             dic[char] = i
    #             i += 1

    # fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

    # names = list(dic.keys())
    # values = list(dic.values())

    # # for i in range(len(dic)):
    # #     plt.plot(names[i], values[i])
    # #     print(names[i], values[i])
    # #     i = i + 1
    # axs[0].bar(names, values)
    # axs[1].scatter(names, values)
    # axs[2].plot(names, values)

    # print(dic)
    # # print(x)
    # print(len(x))
    # fig.suptitle('Test Plotting')

    # axs.bar(alphabet, 80000)

    # plt.show()


file.close()
