import pygame
import random
from player import Player
from enemy import Enemy
from bullet import Bullet
from settings import screen_width, screen_height, white, red, black

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

class Game:
    def __init__(self):
        self.screen = screen
        self.clock = clock
        self.font = font

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
        score_text = self.font.render(f"Score: {self.score}", True, white)
        lives_text = self.font.render(f"Lives: {self.lives}", True, white)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (screen_width - 150, 10))

    def game_over(self):
        over_font = pygame.font.SysFont(None, 50)
        game_over_text = over_font.render("Game Over! Press R to Restart", True, red)
        self.screen.blit(game_over_text, (screen_width // 4, screen_height // 2))

    def game_loop(self):
        while self.running:
            self.screen.fill(black)  # Siyah arkaplan

            if self.lives <= 0:
                self.game_over()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.__init__()
                    elif event.type == pygame.QUIT:
                        self.running = False
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

            for bullet in list(self.bullets):
                enemies_hit = pygame.sprite.spritecollide(bullet, self.enemies, True)
                if enemies_hit:
                    self.score += 10
                    bullet.kill()

            self.show_score_lives()
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
