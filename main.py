import pygame

# setup pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")

is_running = True

while is_running:
    # game loop / event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # draw game
    display_surface.fill('yellow')


    pygame.display.update()


pygame.quit()