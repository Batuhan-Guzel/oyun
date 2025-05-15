import pygame
import random
from settings import screen_width, screen_height

class StrongEnemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/enemyGreen1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(-150, -50)

        self.health = 30
        self.speed = 1
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
        self.rect.y = random.randint(-150, -50)
        self.health = 20

    def hit(self, damage=1):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            return True
        return False
