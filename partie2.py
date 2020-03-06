#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Un annuaire en format liste [] des dictionaires {}
class model:
    """ classe de modele de donnée"""
    def __init__(self):
        self.annuaire = [
        {'prenom':'Ahmed', 'nom':'Mahdi', 'tel':'0778787887'},
        {'prenom':'Mohamed', 'nom':'Mahdi','tel':'0778787887'},
        {'prenom':'Mounir', 'nom':'Katibi','tel':'0778787887'},
        {'prenom':'Noui', 'nom':'Brahimi','tel':'0778787887'},
        ]

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
        personnes = []
        for persn in self.annuaire:
            # afficher toutes les personnes qui ont le nom donné
            if persn['nom'] == nom:
                personnes.append(persn)
        #retourner une liste de dictionnaires
        return personnes


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

def controleur():
    data_model = model()
    affichage = view()

    """ rechercher un nom """
    #nom = affichage.input()
    personnes = data_model.get_all()
    affichage.output(personnes)

if __name__ == '__main__':
    controleur()