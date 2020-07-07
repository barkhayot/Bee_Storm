#shmup game
import pygame
from pygame import *
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("test")
clock = pygame.time.Clock()


#font for text 
over_font = pygame.font.Font("cherry.ttf", 46)
def game_over():
    # = pygame.font.Font("cherry.ttf", 46)
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

def draw_text(surf, text, size, x, y ):
    font = pygame.font.Font("cherry.ttf", 46)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect =  text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    #sprite for player 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.radius = 25
        self.rect.centerx = 800 / 2
        self.rect.bottom = 600 - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    #sprite for anemy 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = anemy_img
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 / 2)
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x +=self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 600 + 10:
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = random.randrange(-100, 40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    #sprite for bulltes 
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = nut_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
         #kill if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()




# backgroud 

background = pygame.image.load("cloudvwe.jpg")
background_rect = background.get_rect()
player_img = pygame.image.load("person.png")
anemy_img = pygame.image.load("bee.png")
nut_img = pygame.image.load("nut.png")

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0

#loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    
    all_sprites.update()
    #check if the bullet hits the mob 
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 5
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    
    #check if the mob hit the player 

    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        game_over()
        running = False


    screen.fill((0, 0, 0))
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 100, 400, 10)
    pygame.display.flip()
    
pygame.quit()