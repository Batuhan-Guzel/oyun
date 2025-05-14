from main import screen, screen_width, screen_height, white, red, black, font  
from player import Player
from enemy import Enemy
from bullet import Bullet
import pygame
import random

clock = pygame.time.Clock()

class Game:
    def _init_(self):
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        for _ in range(5):
            enemy = Enemy()
            self.all_sprites.add(enemy)
            self.enemies.add(enemy)

        self.score = 0
        self.lives = 3
        self.running = True

    def show_score_lives(self):
        score_text = font.render(f"Score: {self.score}", True, white)
        lives_text = font.render(f"Lives: {self.lives}", True, white)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (screen_width - 150, 10))

    def game_over(self):
        game_over_text = font.render("Game Over! Press R to Restart", True, red)
        screen.blit(game_over_text, (screen_width // 4, screen_height // 2))

    def game_loop(self):
        global score, lives
        while self.running:
            screen.fill(black)

            if self.lives <= 0:
                self.game_over()
                pygame.display.update()
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top)
                        self.all_sprites.add(bullet)
                        self.bullets.add(bullet)

            self.all_sprites.update()

            for bullet in self.bullets:
                enemies_hit = pygame.sprite.spritecollide(bullet, self.enemies, True)
                if enemies_hit:
                    self.score += 10
                    bullet.kill()

            self.show_score_lives()

            self.all_sprites.draw(screen)

            self.enemies.update()

            pygame.display.update()
            clock.tick(60)

        pygame.quit()

if __name__ == "_main_":
    game = Game()
    game.game_loop()