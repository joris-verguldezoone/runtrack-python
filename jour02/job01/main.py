# Créer une classe “Livre” avec comme attribut un “titre” qu’elle reçoit en paramètre à la
# construction et une référence vers une classe “Auteur”. Ajouter une méthode “print”
# permettant d’afficher dans le terminal le titre du livre. Créer une classe “Auteur” héritant
# de la classe “Personne” recevant un nom et un prénom en paramètre de construction.
# La classe auteur devra posséder une collection de livres nommée "œuvre" en attribut
# ainsi qu’une méthode “listerOeuvre” affichant dans le terminal la liste des livres écrits
# par l’auteur. Ajouter à la classe Auteur une méthode “ecrireUnLivre” prenant en
# paramètre un titre de livre à écrire et générer une instance de la classe livre avec ce
# titre. Ajouter ce nouveau livre à l’oeuvre de l’auteur
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

class Auteur(Personne):
    def __init__(self,oeuvre):
        self.oeuvre = oeuvre

    def listerOeuvre(self):
        for livre in self.oeuvre:
            print(livre)

    def ecrireUnLivre(self,titre,auteur):
        obj = Livre(titre,auteur)
        self.oeuvre.append(obj)
        self.titre = titre 
        
class Livre:
    def __init__(self, titre, Auteur):
        self.titre = titre
        self.Auteur = Auteur
    
    def print(self):
        print(self.titre)

auteur = Auteur(['MathisSportCollection', 'Le levé de mathis'])
livre = Livre("Adrien et les septs nains",'Jojjj')

auteur.ecrireUnLivre("grojjjjjj",auteur)
auteur.listerOeuvre()


livre.print()