import pygame
from game import Game
pygame.init()

#generer la fenetre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')


#Charger le jeu
game = Game()

running = True

#boucle tant que cette condition est vrai
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)
    
    #recuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    #appliquer l'ensemble d'image du projectile
    game.player.all_projectiles.draw(screen)

    #verifier si le joueur souhaiet aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

    #mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            #detecter le tir avec espace
            if event.key == pygame.K_SPACE:
                game.player.lauch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
