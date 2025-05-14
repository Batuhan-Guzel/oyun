# enemy.py

import pygame
import random
from settings import screen_width, screen_height, red

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Boyut
        self.image.fill(red)  # Renk
        self.rect = self.image.get_rect()  # rect özelliğini doğru şekilde ayarladık
        self.rect.x = random.randrange(0, screen_width - 50)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.rect.x = random.randrange(0, screen_width - 50)
            self.rect.y = random.randrange(-100, -40)
