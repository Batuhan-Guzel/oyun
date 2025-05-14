# player.py

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Oyuncu için bir yüzey
        self.image.fill((0, 255, 0))  # Oyuncu rengini yeşil yapıyoruz
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)  # Başlangıç pozisyonu

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
