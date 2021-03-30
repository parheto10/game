import pygame
#cree un Classe Mere Game qui va representer notre Jeu
from player import Player


class Game():
    #initialisation de la class Game
    def __init__(self):
        # charger le Joueur
        self.player = Player()
        self.pressed = {}