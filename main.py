import pygame
from random import randint

# setup pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

# plain surface
surf = pygame.Surface((50, 50))
surf.fill('yellow')
x = 0

# image surface
player_surf = pygame.image.load('./images/player.png').convert_alpha()
star = pygame.image.load('./images/star.png').convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]



is_running = True

while is_running:
    # game loop / event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # draw game
    display_surface.fill('darkgray')
    x+=.1
    #display_surface.blit(surf, (x, 200))
    display_surface.blit(player_surf, (x, 300))
    for pos in star_pos:
        display_surface.blit(star, pos)
    


    pygame.display.update()


pygame.quit()