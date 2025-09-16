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

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

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
star_surf = pygame.image.load('./images/star.png').convert_alpha()
for i in range(20):
    Star(all_sprite, star_surf)
player = Player(all_sprite)

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
    
    # update 
    all_sprite.update(dt)

    # draw game
    display_surface.fill('darkgray')  # --bg
    all_sprite.draw(display_surface)

    pygame.display.update()


pygame.quit()