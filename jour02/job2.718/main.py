# Créer une classe “Client” héritant de “Personne”, prenant en paramètre un nom et un
# prenom.
# Créez une classe “Bibliotheque” avec comme attributs un nom et un catalogue: une
# collection de livres ou chaque livre est associé à une quantité (représenté par un
# nombre entier). Ajoutez les méthodes suivantes :
# - acheterLivre: Prenant en paramètre un objet auteur, le nom d’un livre ainsi qu’un
# nombre entier représentant une quantité. Si le livre existe bien dans l'œuvre de
# l’auteur, ajouter ce livre au catalogue de la bibliothèque avec la quantité
# correspondante.
# - inventaire: Une méthode qui affiche dans le terminal les titres des livres présents
# dans le catalogue ainsi que leur quantité.
# - louer: Cette méthode reçoit en paramètres une instance d’objet “Client” ainsi que
# le nom d’un livre. Si le livre existe et est en stock, ajoutez ce livre à la collection
# de livre du client et tenez à jour la quantité de ce livre dans la bibliothèque.
# - rendreLivres: Une méthode qui prend un “Client” en paramètre et qui récupère
# tous les livres de ce dernier et les ajoute au catalogue de la bibliothèque.
# Ajouter à la classe “Client” un attribut collection étant une collection de livres et ajouter
# la méthode inventaire qui affiche dans le terminal les titres des livres en possession du
# client.
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
        
class Client(Personne):
    def __init__(self,nom, prenom):
        self.nom = nom
        self.prenom = prenom 

class Bibliotheque:
    def __init__(self,nom , catalogue):
            self.nom = nom 
            self.catalogue = catalogue # devra etre une collection {number: string}

    def acheterLivre(self,Auteur, nomLivre, quantité): 
        for oeuvre in Auteur.oeuvre:
            if(nomLivre == oeuvre ):
                bibliothèque = Bibliotheque
                # bibliothèque.
    def inventaire(self):
        for key, oeuvre in self.catalogue.items():
            print(oeuvre + ' | Quanditité : '+str(key))
    
    # def louer(client, titre): #instance de Client en appel 

# - acheterLivre: Prenant en paramètre un objet auteur, le nom d’un livre ainsi qu’un
# nombre entier représentant une quantité. Si le livre existe bien dans l'œuvre de
# l’auteur, ajouter ce livre au catalogue de la bibliothèque avec la quantité
# correspondante.
# - inventaire: Une méthode qui affiche dans le terminal les titres des livres présents
# dans le catalogue ainsi que leur quantité.*

bibliotheque = Bibliotheque('Labibi de Jojj', {0:'Akira', 1:'GITS',2:'Requiem'})
bibliotheque.inventaire() 
bibliothèque.acheterLivre()