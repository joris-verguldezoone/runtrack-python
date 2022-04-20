# Créez une classe “Personne” avec les attributs “nom”, “prenom”. Ajoutez une méthode
# “SePresenter()” qui affichera dans le terminal le nom et le prénom de la personne.
# Ajoutez aussi un constructeur prenant en paramètres de quoi donner des valeurs
# initiales aux attributs “nom” et “prenom”. Instanciez plusieurs personnes avec les
# valeurs de construction de votre choix et faites appel à la méthode “SePresenter()” afin
# de vérifier que tout fonctionne correctement. Ajouter un “accesseur” et un “mutateur”
# pour chacun des attributs.

from xml.dom import NoModificationAllowedErr


class Personne:
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print(self.nom + ' ' + self.prenom)

    def accesseur(self):
        print(self.nom + ' ' + self.prenom)

    def mutateur(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom

p1 = Personne("Jean-François-Pilatre", "De Rosier")
p2 = Personne('Adrien', 'Coquillat')
p3 = Personne('Dorian', 'Palace')

p1.SePresenter()
p1.mutateur('Jojjj','Verrr')

p1.SePresenter()