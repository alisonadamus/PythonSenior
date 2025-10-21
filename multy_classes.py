import pygame
import random

class Player():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x -= 5
        if key[pygame.K_RIGHT]:
            self.x += 5
        if key[pygame.K_UP]:
            self.y -= 5
        if key[pygame.K_DOWN]:
            self.y += 5


class Enemy:
    def __init__(self):
        x = random.randint(0, 400)
        y = random.randint(0, 300)
        self.rect = pygame.Rect(x, y, 40, 40)
        self.color = (255, 0, 0)
        self.speed = random.choice([2, 3, 4])
        self.direction = random.choice([-1, 1])

    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.direction *= -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(400, 300, 20, (35, 255, 150))
enemies = [Enemy() for _ in range(5)]
player.draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((255,255,5))
    player.move()
    player.draw()

    for enemy in enemies:
        enemy.update()
        enemy.draw(screen)
        if enemy.rect.x in range(player.x - 30, player.x + 30) and enemy.rect.y in  range(player.y - 30, player.y + 30):
            enemy.color = (0, 255, 0)

    pygame.display.flip()
    clock.tick(60)