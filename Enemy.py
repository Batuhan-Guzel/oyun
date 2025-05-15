import pygame
import random
from settings import screen_width, screen_height

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/enemyRed1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)

        self.health = random.randint(5, 10)
        self.speed = max(1, 5.0 - self.health * 0.2)

        self.move_delay = 3
        self.move_counter = 0

    def update(self):
        self.move_counter += 1
        if self.move_counter >= self.move_delay:
            self.rect.y += self.speed
            self.move_counter = 0

        if self.rect.top > screen_height:
            self.reset_position()

    def reset_position(self):
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.health = random.randint(5, 10)
        self.speed = max(0.5, 3.0 - self.health * 0.2)

    def hit(self, damage=1):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            return True
        return False
