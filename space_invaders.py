import pygame
import random

# Initialisierung von pygame
pygame.init()

# Bildschirmgrößen und Farben
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Spieler
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Alien
alien_width = 50
alien_height = 50
alien_speed = 3
aliens = []

# Projektile
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []

# Spielschleife
def game_loop():
    global player_x, player_y
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Bewegung des Spielers
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])
        
        # Bewegung der Schüsse
        for bullet in bullets[:]:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullets.remove(bullet)

        # Bewegung der Aliens
        for alien in aliens:
            alien[1] += alien_speed
        
        # Kollisionen und Rendering
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))  # Spieler
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, (bullet[0], bullet[1], bullet_width, bullet_height))  # Schüsse
        for alien in aliens:
            pygame.draw.rect(screen, (255, 0, 0), (alien[0], alien[1], alien_width, alien_height))  # Aliens

        pygame.display.flip()
        clock.tick(60)

# Aliens erzeugen
def generate_aliens():
    global aliens
    for i in range(5):  # 5 Reihen von Aliens
        for j in range(10):  # 10 Aliens pro Reihe
            aliens.append([j * (alien_width + 10), i * (alien_height + 10)])

generate_aliens()

if __name__ == "__main__":
    game_loop()
    pygame.quit()
