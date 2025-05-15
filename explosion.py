import pygame
import os

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()

        base_path = os.path.dirname(__file__)
        sprite_sheet_path = os.path.join(base_path, 'assets', 'bom.jpeg')
        sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()

        self.frames = []
        frame_count = 6
        frame_width = sprite_sheet.get_width() // frame_count
        frame_height = sprite_sheet.get_height()

        # Yeni boyutları belirle (örneğin yarı yarıya küçült)
        new_width = frame_width // 2
        new_height = frame_height // 2

        for i in range(frame_count):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame_image = sprite_sheet.subsurface(rect)
            scaled_frame = pygame.transform.scale(frame_image, (new_width, new_height))
            self.frames.append(scaled_frame)

        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 100

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.current_frame]
