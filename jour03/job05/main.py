# Écrire un programme qui parcourt le fichier “data.txt” et qui compte le nombre
# d'occurrence de chaque lettre (Minuscules et Capitales comptent pour la même lettre).
# A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage
# d’apparition de chaque lettre.


import re
import matplotlib.pyplot as plt
import numpy as np


file = open('data.txt', 'r')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x = re.findall("[A-z]",  file.read())
dic = {}
for char in alphabet:
    i = 0
    for letter in x:
        if (char == letter):
            dic[char] = i
            i += 1

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

names = list(dic.keys())
values = list(dic.values())


# for i in range(len(dic)):
#     plt.plot(names[i], values[i])
#     print(names[i], values[i])
#     i = i + 1
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)

print(dic)
# print(x)
print(len(x))
fig.suptitle('Test Plotting')


# axs.bar(alphabet, 80000)


plt.show()


file.close()
