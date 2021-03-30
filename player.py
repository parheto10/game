import pygame

from projectile import Projectile


class Player(pygame.sprite.Sprite):
    #initialisation de notre class Joueur
    def __init__(self):
        super(Player, self).__init__()
        self.sante = 100 #initialisation de la santé du joueur
        self.max_sante = 100 #initialisation de la santé max du joueur
        self.attack = 10 #initialisation du point d'impacte du Joueur
        self.vitesse = 2 #initialisation du point de la vitesse du Joueur
        self.all_projectiles = pygame.sprite.Group() # Groupe de Projectile
        self.image = pygame.image.load('assets/player.png')
        #recuperation de coordonnées du Joueur
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 500

    def lunch_projectile(self):
        #creer une nouvelle instance de la classe Projectile
        # projectile = Projectile()
        self.all_projectiles.add(Projectile(self))


    def move_droite(self):
        self.rect.x += self.vitesse

    def move_gauche(self):
        self.rect.x -= self.vitesse
