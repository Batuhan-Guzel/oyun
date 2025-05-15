import pygame
import sys
import os

def main():
    # Ses sistemi için ön yükleme (mutlaka pygame.init() öncesi olmalı)
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()

    # Mixer durumu ve kanal sayısını yazdır
    mixer_init = pygame.mixer.get_init()
    channels = pygame.mixer.get_num_channels()
    print(f"Mixer başlatıldı mı? {mixer_init}")
    print(f"Mixer kanal sayısı: {channels}")

    # Pencere aç
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Pygame Ses Testi")

    # Ses dosyasının yolu (projenin kök dizinine göre ayarla)
    sound_path = os.path.join('assets', 'sounds', 'explosion.wav')

    # Ses dosyasını yükle
    try:
        sound = pygame.mixer.Sound(sound_path)
        print(f"Ses dosyası başarıyla yüklendi: {sound_path}")
    except Exception as e:
        print(f"Ses dosyası yüklenirken hata: {e}")
        pygame.quit()
        sys.exit()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Space tuşuna basıldı, ses çalıyor...")
                    sound.set_volume(1.0)  # Maksimum ses
                    sound.play()

                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill((30, 30, 30))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
