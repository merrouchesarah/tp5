#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from xml.dom import minidom


class modele:
    def __init__(self):
        #self.annuaire = []
        try:
            myfile = minidom.parse("listetudiants.xml")
        except:
            print("Can't open DataFile")
            sys.exit()

        liste = myfile.getElementsByTagName('etudiant')

        cpt = 0
        self.tabEtud=[]

        for etudiant in liste:
            nom = etudiant.getElementsByTagName('nom')[0]
            mat = etudiant.getElementsByTagName('matricule')[0]
            prenom = etudiant.getElementsByTagName('prenom')[0]
            moyS1 = etudiant.getElementsByTagName('moyS1')[0]
            moyS2 = etudiant.getElementsByTagName('moyS2')[0]
            moyAnnuel= etudiant.getElementsByTagName('moyAnnuel')[0]
            creditS1 = etudiant.getElementsByTagName('creditS1')[0]
            creditS2 = etudiant.getElementsByTagName('creditS2')[0]
            uniteaqu = etudiant.getElementsByTagName('uniteaqu')[0]
            mention = etudiant.getElementsByTagName('mention')[0]

            etudiants = {}
            etudiants["nom"] = nom.firstChild.data
            etudiants["prenom"] = prenom.firstChild.data
            etudiants["matricule"] = mat.firstChild.data
            etudiants["moyS1"] = moyS1.firstChild.data
            etudiants["moyS2"] = moyS2.firstChild.data
            etudiants["moyAnnuel"] = moyAnnuel.firstChild.data
            etudiants["creditS1"] = creditS1.firstChild.data
            etudiants["creditS2"] = creditS2.firstChild.data
            etudiants["uniteaqu"] = uniteaqu.firstChild.data
            etudiants["mention"] = mention.firstChild.data
            self.tabEtud.append(etudiants)
            cpt +=1

    def get_all(self):
        # La liste des etudiants trouvées
        etudiants = []
        for etud in self.tabEtud:
            # afficher toutes les etudiants
            etudiants.append(etud)
            # un tableaux avec des nom des champs
        return etudiants


    def rechercher(self,nom):
        etud=[]
        for e in self.tabEtud:
            if e['nom']== nom :
                etud.append(e)
        return etud

    def ajouter(self, matricule, nom, prenom, moyS1,moyS2,moyAnnuel,creditS1,creditS2,uniteaqu,mention):
        """ ajouter un etudiant """

        etudiant = {}
        etudiant["nom"] = nom
        etudiant["prenom"] = prenom
        etudiant["matricule"] = matricule
        etudiant["moyS1"] = moyS1
        etudiant["moyS2"] = moyS2
        etudiant["moyAnnuel"] = moyAnnuel
        etudiant["creditS1"] = creditS1
        etudiant["creditS2"] = creditS2
        etudiant["uniteaqu"] = uniteaqu
        etudiant["mention"] = mention

        self.tabEtud.append(etudiant)

    def calcul(self):
        nb_etudiants=len(self.tabEtud)
        bestMoy = 0
        for l in self.tabEtud:

            if float(l['moyAnnuel']) > bestMoy:
                bestMoy = float(l['moyAnnuel'])
        badMoy = 20
        for l in self.tabEtud:
            if float(l['moyAnnuel']) < badMoy:
                badMoy = float(l['moyAnnuel'])
        somme = 0
        for l in self.tabEtud:
            somme = somme + float(l['moyAnnuel'])
        moyenne = round((somme/nb_etudiants),2)
        return(nb_etudiants,bestMoy,badMoy,moyenne)

class view:
    def __init__(self):
        pass
    def input(self):

        print("Recherche d'un etudiant")
        print("Introduire Un nom")
        nom = input()
        return nom
    def output(self, etudiants):

        print("La liste des etudiants trouvés")
        #print(" %d etudiants trouvées"%len(etudiants))
        for etu in etudiants:
            print(etu['matricule'], etu['nom'], etu['prenom'],etu['moyS1'],etu['moyS2'],etu['moyAnnuel'],
                  etu['creditS1'],etu['creditS2'],etu['uniteaqu'],etu['mention'])

    def input_ajout(self):

        print("Ajout d'un etudiant")
        print("Introduire Un matricule")
        matricule = input()
        print("Introduire Un nom")
        nom = input()
        print("Introduire Un prenom")
        prenom = input()
        print("Introduire moyenne s1")
        moyS1 = input()
        print("Introduire moyenne s2")
        moyS2= input()
        print("Introduire moyenne annuel")
        moyAnnuel = input()
        print("Introduire credits s1")
        creditS1= input()
        print("Introduire credits s2")
        creditS2 = input()
        print("unite aquise? oui ou non?")
        uniteaqu = input()
        print("quelle est votre mention")
        mention = input()
        return (matricule,nom, prenom, moyS1,moyS2,moyAnnuel,creditS1,creditS2,uniteaqu,mention)

    def output_calcul(self,nb,best,bad,moyenne):
        print("Les statistiques:")
        print("Le nombre des etudiants :", nb)
        print("La meilleur moyenne :", best)
        print("La mauvaise moyenne :", bad)
        print("La moyenne de la classe:", moyenne)

class controleur:
    def __init__(self):
        """ constructeur du controleur"""
        self.data_model = modele()
        self.affichage = view()
    def rechercher(self):
        """ rechercher un nom """
        nom = self.affichage.input()
        etudiants = self.data_model.rechercher(nom)
        self.affichage.output(etudiants)

    def ajouter(self):

        matricule,nom, prenom, moyS1,moyS2,moyAnnuel,creditS1,creditS2,uniteaqu,mention = self.affichage.input_ajout()
        self.data_model.ajouter(matricule,nom, prenom, moyS1,moyS2,moyAnnuel,creditS1,creditS2,uniteaqu,mention)
        etudiants = self.data_model.get_all()
        self.affichage.output(etudiants)
        #tel = input()
        return (matricule,nom, prenom, moyS1,moyS2,moyAnnuel,creditS1,creditS2,uniteaqu,mention)

    def calcul(self):
        nb,best,bad,moyenne= self.data_model.calcul()
        self.affichage.output_calcul(nb,best,bad,moyenne)

if __name__ == '__main__':

    controleur().calcul()



