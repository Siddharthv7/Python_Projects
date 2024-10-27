import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Space Shooter with Particle Effects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Frame rate
FPS = 60
clock = pygame.time.Clock()

# Load assets
player_img = pygame.image.load("spaceship.png").convert_alpha()
enemy_img = pygame.image.load("enemy.png").convert_alpha()
bullet_img = pygame.image.load("bullet.png").convert_alpha()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5
        if keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(bullet)

    def draw(self):
        screen.blit(self.image, self.rect)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemy_img, (40, 30))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speedy = random.randint(2, 6)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(0, WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(2, 6)

    def draw(self):
        screen.blit(self.image, self.rect)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

    def draw(self):
        screen.blit(self.image, self.rect)

# Particle effect class for explosion
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = random.uniform(0, math.pi * 2)
        self.speed = random.uniform(2, 6)
        self.lifetime = random.randint(20, 40)
        self.radius = random.randint(2, 4)
        self.color = YELLOW

    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.lifetime -= 1

    def draw(self):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Explosion manager to handle particles
class Explosion:
    def __init__(self, x, y):
        self.particles = []
        for _ in range(20):
            self.particles.append(Particle(x, y))

    def update(self):
        self.particles = [p for p in self.particles if p.lifetime > 0]
        for particle in self.particles:
            particle.update()

    def draw(self):
        for particle in self.particles:
            particle.draw()

# Initialize player, enemy, and groups
player = Player()
players = pygame.sprite.Group(player)
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
explosions = []

for _ in range(8):
    enemy = Enemy()
    enemies.add(enemy)

# Game loop
running = True
while running:
    clock.tick(FPS)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update objects
    player.update()
    bullets.update()
    enemies.update()

    for explosion in explosions:
        explosion.update()

    # Check for collisions
    for bullet in bullets:
        hit = pygame.sprite.spritecollideany(bullet, enemies)
        if hit:
            explosion = Explosion(hit.rect.centerx, hit.rect.centery)
            explosions.append(explosion)
            hit.kill()
            bullet.kill()

    # Draw everything
    screen.fill(BLACK)
    players.draw(screen)
    bullets.draw(screen)
    enemies.draw(screen)
    for explosion in explosions:
        explosion.draw()

    pygame.display.flip()

pygame.quit()
