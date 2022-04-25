# Créer un programme qui parcourt le contenu du fichier “domains.xml” et qui compte le
# nombre d’extension de domaines qui s’y trouvent (.com, .net, etc ...).
import re

file = open('domains.xml', 'r')
file2 = open('domains.xml', 'r')  # triche ?

net = '.net'
com = '.com'
x = re.findall(".net",  file.read())
y = re.findall(".com",  file2.read())
print(len(x))
print('x')
print(len(y))
print('y')
file.close()
