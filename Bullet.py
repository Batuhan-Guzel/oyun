from main import screen_width, screen_height, white  
import pygame


class Bullet(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((5, 10))  
        self.image.fill(white)  
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  
        self.speed = 7  

    def update(self):
        self.rect.y -= self.speed  
        if self.rect.bottom < 0:  
            self.kill()
