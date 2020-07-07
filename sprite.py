#shmup game
import pygame
from pygame import *
import random

class Player(pygame.sprite.Sprite):
    #sprite for player 
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("zombie.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (800 / 2, 600 / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > 800:
            self.rect.right = 0


pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("test")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    
pygame.quit()