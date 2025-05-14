from settings import screen_width, screen_height, red  
import pygame
import random  


class Enemy(pygame.sprite.Sprite):   
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50))  
        self.image.fill(red)  
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, screen_width - 50)
        self.rect.y = random.randrange(-100, -40)  
        self.speed = random.randint(1, 3)  

    def update(self):
        self.rect.y += self.speed 
        if self.rect.top > screen_height:  
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(0, screen_width - 50)