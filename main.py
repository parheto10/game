import pygame
#initialisation
from game import Game
pygame.init()
# generer la fenetre principale de notre Jeu avec un Titre
pygame.display.set_caption("Comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#Ajouter un Background
background = pygame.image.load('assets/bg.jpg')

#charger notre Jeu
game = Game()

#affichage continue de la fenetre
running = True

#boocle tant que le Running est vrai
while running:

    # appliquer le Background
    screen.blit(background, (0, -200))

    #appliquer l'image du joueur sur la fentre du jeu
    screen.blit(game.player.image, game.player.rect)

    #recuperer les Projectiles lancer du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #Appliquer l'ensemble des Image de Mon groupe de Projectiles
    game.player.all_projectiles.draw(screen)

    #Verifier si le Joueur shte aller a Droite ou a Gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_droite()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_gauche()

    #recuperer les Coordonnees du Joueur
    print(game.player.rect.x)

    #mettre a jour l'écran
    pygame.display.flip()

    #Action de fermeture de la fenetre par le Joueur
    for event in pygame.event.get():
        # si le joueur click sur le Bouton Fermer
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du Jeux .....")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #verifier si le joueur appui sur Espace pour balancer un Projectile
            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            # #verifier la touche Appuyer
            # if event.key == pygame.K_RIGHT:
            #     game.player.move_droite()
            # elif event.key == pygame.K_LEFT:
            #     game.player.move_gauche()

