from settings import screen_width, screen_height, white  
import pygame


class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50)) 
        self.image.fill(white)  
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)  
        self.speed = 5  

    def update(self):
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed
