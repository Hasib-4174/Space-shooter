import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.speed = 300 
        self.direction = pygame.math.Vector2(1, 1)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center +=  self.direction * self.speed * dt
        #print('player being updated', end='  ')

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('fire laser', end=' ')

# setup pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

# plain surface
surf = pygame.Surface((50, 50))
surf.fill('yellow')

all_sprite = pygame.sprite.Group()
player = Player(all_sprite)
#all_sprite.add(player)

# player surface
#player_surf = pygame.image.load('./images/player.png').convert_alpha()
#player_pos = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
#player_direction = pygame.math.Vector2()
#player_speed = 400 


star = pygame.image.load('./images/star.png').convert_alpha()
star_pos = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for _ in range(20)]

meteor_surf = pygame.image.load('./images/meteor.png').convert_alpha()
meteor_pos = meteor_surf.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load('./images/laser.png').convert_alpha()
laser_pos = laser_surf.get_frect(bottomleft=(20,WINDOW_HEIGHT - 20))

is_running = True

while is_running:
    dt = clock.tick() / 1000
    #print(f'fps: {int(clock.get_fps()):<4d} Directin: {player_direction} Mgnitude: {(player_direction * player_speed).magnitude()}')
    #print(f'fps: {int(clock.get_fps()):<4d}')
    # game loop / event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            print('key: 1')
        #if event.type == pygame.MOUSEMOTION:
            #player_pos.center = event.pos
            #print(event.pos)
    
    all_sprite.update(dt)
    #input
    #print(pygame.mouse.get_rel())
    #player_pos.center = pygame.mouse.get_pos()

    #keys = pygame.key.get_pressed()
    #player_direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
    #player_direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    #player_direction = player_direction.normalize() if player_direction else player_direction
    #player_pos.center += player_direction * player_speed * dt


    #recent_key = pygame.key.get_just_pressed()
    #if recent_key[pygame.K_SPACE]:
        #print('fire laser')

    

    # draw game
    display_surface.fill('darkgray')  # --bg
    for pos in star_pos:
        display_surface.blit(star, pos)   # starts

    display_surface.blit(meteor_surf, meteor_pos)  # meteor
    display_surface.blit(laser_surf, laser_pos)    # laser

    #display_surface.blit(player_surf, player_pos)    # player_surf
    #display_surface.blit(player.image, player.rect)
    all_sprite.draw(display_surface)

    pygame.display.update()


pygame.quit()