# # créé par Albert Cloutier
# # groupe 406
# # exercice classes 1.1

# class StringFoo:
#     def __init__(self):
#         self.msg = ""
#
#     def greetings(self):
#         print(self.msg)
#
#
#     def set_string(self, message, majuscule):
#         grandeur = 10
#         self.msg = message
#
#     def print_string(self):
#         print(self.msg.upper())
#
#
#
# str1 = StringFoo()
# str1.msg = "Pomme"
# str1.greetings()
# str1.print_string()
#
# str1.set_string("Patate", 99)
# str1.greetings()
#


# partie 2

# class Rectangle:
#     def __init__(self, longueur, largeur):
#         self.longueur = longueur
#         self.largeur = largeur
#         self.aire = 0
#
#     def calcul_aire(self):
#         self.aire = self.longueur * self.largeur
#
#     def afficher_infos(self):
#         print(self.aire)
#
#
# rect_1 = Rectangle(5, 7)
#
# rect_1.calcul_aire()
# rect_1.afficher_infos()


# ctrl + "/" pour commenter

# partie 3

# from math import pi
#
#
# class Cercle:
#     def __init__(self, rayon):
#         self.rayon = rayon
#         self.aire = 0
#         self.circonference = 0
#
#     def calcul_aire(self):
#         self.aire = pi * self.rayon * self.rayon
#
#     def calcul_circonference(self):
#         self.circonference = 2 * pi * self.rayon
#
#     def afficher_infos(self):
#         print(f"{self.aire} aire")
#
#
# cercle_1 = Cercle(2)
# cercle_1.calcul_circonference()
# cercle_1.calcul_aire()
# cercle_1.afficher_infos()

# partie 4
from random import randint


class Hero:
    def __init__(self, nom):
        self.vie = randint(1, 10) + randint(1, 10)
        self.attaque = randint(1, 6)
        self.defense = randint(1, 6)
        self.nom = nom

    def faire_attaque(self):
        return self.attaque + randint(1, 6)

    def recevoir_dommages(self, dommage):
        self.vie -= dommage - self.defense

    def est_vivant(self):
        return self.vie > 0


hero = Hero("Albert")
if hero.est_vivant():
    print("vivant")
