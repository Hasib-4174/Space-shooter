import pygame
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('./images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.speed = 300 
        self.direction = pygame.math.Vector2(1, 1)
        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 200

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            #print(current_time)
            if current_time >= self.laser_shoot_time + self.cooldown_duration:
                self.can_shoot = True
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center +=  self.direction * self.speed * dt
        #print('player being updated', end='  ')

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            #print('fire laser', end=' ')
            Laser(laser_surf, self.rect.midtop, all_sprite)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 400 * dt
        if self.rect.bottom < 0:
            self.kill()
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, groups, pos):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        #self.start_time = pygame.time.get_ticks()
        #self.lifetime = 3000
        self.speed = randint(300, 400)
        self.direction = pygame.math.Vector2(uniform(-.5, .5), 1)
    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt 
        #if pygame.time.get_ticks() >= self.start_time + self.lifetime:
        if self.rect.top >= 720:
            self.kill()


# setup pygame
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
is_running = True


# Import
star_surf = pygame.image.load('./images/star.png').convert_alpha()
meteor_surf = pygame.image.load('./images/meteor.png').convert_alpha()
laser_surf = pygame.image.load('./images/laser.png').convert_alpha()

# Sprites
all_sprite = pygame.sprite.Group()
for i in range(20):
    Star(all_sprite, star_surf)
player = Player(all_sprite)

# custom timer -> meteor timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

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
        if event.type == meteor_event:
            #print('meteor & star')
            meteor = Meteor(meteor_surf, all_sprite, (randint(0, WINDOW_WIDTH), randint(-200, -100)))
            meteor.meteor_can_destroy = False
    
    # update 
    all_sprite.update(dt)

    # draw game
    display_surface.fill('darkgray')  # --bg
    all_sprite.draw(display_surface)

    pygame.display.update()


pygame.quit()