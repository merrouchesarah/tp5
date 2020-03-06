#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mvc-ann.py
# Un annuaire en format liste [] des dictionaires {}
annuaire = [
{'prenom':'Ahmed', 'nom':'Mahdi', 'tel':'077878'},
{'prenom':'Mohamed', 'nom':'Rabehi','tel':'06678'},
{'prenom':'Mounir', 'nom':'Mahdi','tel':'0556644'},
{'prenom':'Noui', 'nom':'Brahimi','tel':'067879'},
]
def main():
    # Ce programme permet de recherche le num dans un tableau par son nom, et afficher
    # lire des données a partir du clavier
    print("Recherche d'un telephone")
    print("Introduire Un nom")

    nom = input()

    # nombre d'elements trouvés
    nb_found = 0
    # parcours des noms
    for personne in annuaire:
        # afficher toutes les personnes qui ont le nom donné
        if personne['nom'] == nom:
            print(nom, personne['prenom'], personne['tel'])
            nb_found += 1
    if not nb_found:
        print("ce nom %s n'existe pas "%nom)

if __name__ == '__main__':
    main()