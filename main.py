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
player_pos = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
direction_x = 2
direction_y = -1 
player_direction = pygame.math.Vector2()
player_speed = 400 


star = pygame.image.load('./images/star.png').convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

meteor_surf = pygame.image.load('./images/meteor.png').convert_alpha()
meteor_pos = meteor_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load('./images/laser.png').convert_alpha()
laser_pos = laser_surf.get_frect(bottomleft=(20,WINDOW_HEIGHT - 20))

is_running = True

while is_running:
    dt = clock.tick() / 1000
    print(f'fps: {int(clock.get_fps())}')
    # game loop / event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print('key: 1')
        #if event.type == pygame.MOUSEMOTION:
            #player_pos.center = event.pos
            #print(event.pos)
    
    #input
    #print(pygame.mouse.get_rel())
    #player_pos.center = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
    player_pos.center += player_direction * player_speed * dt
    

    # draw game
    display_surface.fill('darkgray')  # --bg
    for pos in star_pos:
        display_surface.blit(star, pos)   # starts

    display_surface.blit(meteor_surf, meteor_pos)  # meteor
    display_surface.blit(laser_surf, laser_pos)    # laser

    #player_pos.center += player_direction * player_speed * dt
    display_surface.blit(player_surf, player_pos)    # player_surf

    pygame.display.update()


pygame.quit()