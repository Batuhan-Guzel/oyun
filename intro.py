import pygame
import os
import sys
from settings import screen_width, screen_height

class Intro:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.frames = []
        self.load_frames()
        self.index = 0

    def load_frames(self):
        folder = 'assets/intro'
        if not os.path.exists(folder):
            print(f"Intro klasörü bulunamadı: {folder}")
            sys.exit()
        files = sorted(os.listdir(folder))
        for file in files:
            if file.endswith('.png'):
                path = os.path.join(folder, file)
                image = pygame.image.load(path).convert_alpha()
                self.frames.append(image)
        if not self.frames:
            print("Intro kareleri yüklenemedi veya klasörde dosya yok!")
            sys.exit()

    def play(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    running = False

            self.screen.blit(self.frames[self.index], (0, 0))
            pygame.display.update()

            self.index += 1
            if self.index >= len(self.frames):
                running = False

            self.clock.tick(30)
