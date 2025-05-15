from settings import screen_width, screen_height, white, red, black
import pygame
from player import Player
from enemy import Enemy  
from stronge_enemy import StrongEnemy
from bullet import Bullet
from explosion import Explosion

pygame.init()
pygame.font.init()
pygame.mixer.init()  # Ses modülünü başlat

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
        self.explosions = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        for _ in range(5):
            enemy = Enemy()
            self.enemies.add(enemy)
            self.all_sprites.add(enemy)

        self.score = 0
        self.lives = 3
        self.running = True

        self.bullet_damage = 1
        self.show_upgrade_msg = False
        self.upgrade_msg_timer = 0

        self.strong_enemy_timer = pygame.time.get_ticks()
        self.strong_enemy_interval = 15000  # 15 saniye

        # Sesler
        self.shoot_sound = pygame.mixer.Sound('assets/sounds/shoot.wav')
        self.explosion_sound = pygame.mixer.Sound('assets/sounds/explosion.wav')
        pygame.mixer.music.load('assets/sounds/background.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def show_score_lives(self):
        score_text = self.font.render(f"Score: {self.score}", True, white)
        lives_text = self.font.render(f"Lives: {self.lives}", True, white)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (screen_width - 150, 10))

    def show_upgrade_message(self):
        if self.show_upgrade_msg:
            msg_text = self.font.render("Press X to upgrade bullets!", True, white)
            rect = msg_text.get_rect(center=(screen_width//2, screen_height//2))
            self.screen.blit(msg_text, rect)
            if pygame.time.get_ticks() - self.upgrade_msg_timer > 5000:
                self.show_upgrade_msg = False

    def game_over(self):
        over_font = pygame.font.SysFont(None, 50)
        game_over_text = over_font.render("Game Over! Press R to Restart", True, red)
        self.screen.blit(game_over_text, (screen_width // 4, screen_height // 2))

    def wait_for_restart(self):
        waiting = True
        while waiting:
            self.screen.fill(black)
            self.game_over()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

    def game_loop(self):
        while self.running:
            self.screen.fill(black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if self.lives <= 0:
                    continue

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(self.player.rect.centerx, self.player.rect.top, self.bullet_damage)
                        self.bullets.add(bullet)
                        self.all_sprites.add(bullet)
                        self.shoot_sound.play()
                    if event.key == pygame.K_x and self.show_upgrade_msg:
                        self.bullet_damage = 2
                        self.show_upgrade_msg = False

            if self.lives <= 0:
                self.lives = 0
                self.game_over()
                pygame.display.update()
                self.wait_for_restart()
                self.__init__()
                continue

            current_time = pygame.time.get_ticks()
            if current_time - self.strong_enemy_timer > self.strong_enemy_interval:
                self.strong_enemy_timer = current_time
                strong_enemy = StrongEnemy()
                self.enemies.add(strong_enemy)
                self.all_sprites.add(strong_enemy)

            self.all_sprites.update()
            self.explosions.update()

            for bullet in list(self.bullets):
                enemies_hit = pygame.sprite.spritecollide(bullet, self.enemies, False)
                for enemy in list(enemies_hit):
                    bullet.kill()
                    died = enemy.hit(self.bullet_damage) if hasattr(enemy, 'hit') else False
                    if died:
                        self.score += 100
                        explosion = Explosion(enemy.rect.center)
                        self.explosions.add(explosion)
                        self.all_sprites.add(explosion)
                        self.explosion_sound.play()

                        if isinstance(enemy, StrongEnemy):
                            self.show_upgrade_msg = True
                            self.upgrade_msg_timer = pygame.time.get_ticks()

            hits = pygame.sprite.spritecollide(self.player, self.enemies, True)
            if hits and self.lives > 0:
                self.lives -= 1
                if self.lives < 0:
                    self.lives = 0

            while len(self.enemies) < 5:
                enemy = Enemy()
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)

            for enemy in self.enemies:
                health_text = self.font.render(str(enemy.health), True, red)
                text_rect = health_text.get_rect(center=(enemy.rect.centerx, enemy.rect.top - 10))
                self.screen.blit(health_text, text_rect)

            self.all_sprites.draw(self.screen)
            self.explosions.draw(self.screen)
            self.show_score_lives()
            self.show_upgrade_message()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.game_loop()
