import pygame
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)  # Sun Color
BLUE = (0, 0, 255)  # Earth Color
RED = (255, 0, 0)  # Mars Color

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Planet class
class Planet:
    def __init__(self, name, color, distance_from_sun, radius, speed):
        self.name = name
        self.color = color
        self.distance_from_sun = distance_from_sun
        self.radius = radius
        self.speed = speed
        self.angle = 0

    def draw(self, screen):
        # Calculate position using polar coordinates
        x = WIDTH // 2 + self.distance_from_sun * math.cos(self.angle)
        y = HEIGHT // 2 + self.distance_from_sun * math.sin(self.angle)
        pygame.draw.circle(screen, self.color, (int(x), int(y)), self.radius)

    def move(self):
        # Update the angle to simulate movement around the sun
        self.angle += self.speed
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi

# Create planets
sun = Planet("Sun", YELLOW, 0, 30, 0)  # Sun doesn't move
earth = Planet("Earth", BLUE, 150, 10, 0.01)
mars = Planet("Mars", RED, 200, 8, 0.008)

# Main simulation loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)  # Clear screen

    # Draw the sun and planets
    sun.draw(screen)
    earth.draw(screen)
    mars.draw(screen)

    # Move planets
    earth.move()
    mars.move()

    # Event loop to quit simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Refresh the screen
    clock.tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()

