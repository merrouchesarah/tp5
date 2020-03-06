import sys

class model_fichier:
    """ classe de modele de donnée"""

    def __init__(self):
        self.annuaire = []
        try:
            myfile = open("annuaire.txt")
        except:
            print("Can't open DataFile")
            sys.exit()
        lines = myfile.readlines()
        for line in lines:
            line = line.strip('\n')
            fields = line.split('\t')
            personne ={}
            personne["nom"] = fields[0]
            personne["prenom"] = fields[1]
            personne["tel"] = fields[2]
            self.annuaire.append(personne)
        myfile.close()

    def __del__(self):
        """ Destructeur de la classe Modele,
        Il est appelé à la fin de programme
        recharger les donnes dans le fichier """

        try:
            myfile = open("annuaire.txt", "w")
        except:
            print("Can't open DataFile")
            sys.exit()
        for personne in self.annuaire:
            line = personne['nom']+'\t'+ personne['prenom']+'\t'+ personne['tel']+"\n"
            myfile.write(line)
        myfile.close()

    def get_all(self):
        """ rechercher un tel par nom"""
        # La liste des personnes trouvées
        personnes = []
        for persn in self.annuaire:
            # afficher toutes les personnes
            personnes.append(persn)
            # un tableaux avec des nom des champs
        return personnes

    def rechercher(self, nom):
        """ rechecher un tel par nom"""
        # La liste des personnes trouvées
        personnes = {}
        for persn in self.annuaire:
            # afficher toutes les personnes qui ont le nom donné
            if persn['nom'] == nom:
                personnes.append(persn)
        # retourner une liste de dictionnaires
        return personnes

    def ajouter(self, nom, prenom, tel):
        """ ajouter une personne """

        personne = {}
        personne["nom"] = nom
        personne["prenom"] = prenom
        personne["tel"] = tel
        self.annuaire.append(personne)

class view:
    def __init__(self):
        pass
    def input(self):
        """ recuperer le nom à rechercher"""
        print("Recherche d'un telephone")
        print("Introduire Un nom")
        nom = input()
        return nom
    def output(self, personnes):
        """ afficher les informations d'une liste des personnes"""
        print("La liste des noms trouvés")
        print(" %d personnes trouvées"%len(personnes))
        for pers in personnes:
            print(pers['nom'], pers['prenom'], pers['tel'])

    def input_ajout(self):
        """ récupérer le nom à ajouter"""
        #print("nombre a ajouter")
        #nb = input()
        print("Ajout d'une personne")
        print("Introduire Un nom")
        nom = input()
        print("Introduire Un prenom")
        prenom = input()
        print("Introduire Un tel")
        tel = input()
        return (nom, prenom, tel)

class controleur:
    def __init__(self):
        """ constructeur du controleur"""
        # initialiser le model de données
        #~ self.data_model = model()
        self.data_model = model_fichier()
        self.affichage = view()
    def rechercher(self):
        """ rechercher un nom """
        nom = self.affichage.input()
        personnes = self.data_model.rechercher(nom)
        self.affichage.output(personnes)

    def ajouter(self):
        """ rechercher un nom """

        nom, prenom, tel = self.affichage.input_ajout()
        self.data_model.ajouter(nom, prenom, tel)
        personnes = self.data_model.get_all()
        self.affichage.output(personnes)
        #tel = input()
        return (nom, prenom, tel)


if __name__ == '__main__':
    model_fichier().ajouter('Merrouche','Sarah','077625')
