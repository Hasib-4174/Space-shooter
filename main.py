import pygame
from random import randint

# setup pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((50, 50))
surf.fill('yellow')

# image surface
player_surf = pygame.image.load('./images/player.png').convert_alpha()
player_pos = player_surf.get_frect(bottomleft = (0, WINDOW_HEIGHT - 100))
direction_x = 2
direction_y = -1 
player_direction = pygame.math.Vector2(direction_x, direction_y)
player_speed = 300 


star = pygame.image.load('./images/star.png').convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

meteor_surf = pygame.image.load('./images/meteor.png').convert_alpha()
meteor_pos = meteor_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load('./images/laser.png').convert_alpha()
laser_pos = laser_surf.get_frect(bottomleft=(20,WINDOW_HEIGHT - 20))

is_running = True

while is_running:
    dt = clock.tick() / 1000
    print(int(clock.get_fps()))
    # game loop / event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # draw game
    display_surface.fill('darkgray')  # --bg
    for pos in star_pos:
        display_surface.blit(star, pos)   # starts

    display_surface.blit(meteor_surf, meteor_pos)  # meteor
    display_surface.blit(laser_surf, laser_pos)    # laser

    # player --
    if player_pos.left <= 0 or player_pos.right >= WINDOW_WIDTH:
        player_direction.x *= -1
    if player_pos.top <= 0 or player_pos.bottom >= WINDOW_HEIGHT:
        player_direction.y *=-1
    
    player_pos.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_pos)    # player_surf

    pygame.display.update()


pygame.quit()