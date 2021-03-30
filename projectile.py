import pygame

#definir la classe de gestion du Projectile de notre Joueur
class Projectile(pygame.sprite.Sprite):

    #Definir le Constructeur de cette Classe
    def __init__(self, player):
        super(Projectile, self).__init__()
        self.vitesse = 2
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x +120
        self.rect.y = player.rect.y +80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        #faire tourner le projectile sur lui-meme
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.vitesse
        self.rotate()

        #verifier si le projectile est encore sur l'ecran
        if self.rect.x > 1080:
            #supprimer le projectile(lle Détruire)
            self.remove()
            print("projectile detruit ......")

