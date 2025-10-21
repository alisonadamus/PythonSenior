import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 60, 60)
GREEN = (60, 255, 100)

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = BLUE
        self.speed = 5

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Enemy:
    def __init__(self):
        x = random.randint(0, WIDTH - 40)
        y = random.randint(0, HEIGHT - 40)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = RED
        self.speed = random.choice([2, 3, 4])
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2, HEIGHT // 2)
        self.enemies = [Enemy() for _ in range(5)]
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.player.handle_input()
        for enemy in self.enemies:
            enemy.update()

        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                enemy.color = GREEN

    def draw(self):
        screen.fill(WHITE)
        self.player.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
        pygame.display.flip()
game = Game()
game.run()
