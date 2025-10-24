import pygame
import random

class Game():
    def __init__(self, weight, height, player, enemies, price):
        pygame.init()
        self.screen = pygame.display.set_mode((weight, height))
        self.player = player
        self.enemies = enemies
        self.price = price
        self.score = 0
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.handle_event()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def update(self):
        self.player.move()
        for enemy in self.enemies:
            enemy.move()
            if self.player.x in range(enemy.x - 20,enemy.x + 20) and self.player.y in range(enemy.y - 20,enemy.y + 20):
                self.player.x = 20
                self.player.y = 580

        if self.player.x in range(price.x - 25, price.x + 25) and self.player.y in range(price.y - 25, price.y + 25):
            self.score += 1
            self.price.move()


    def draw(self):
        self.screen.fill((15,15,155))
        self.price.draw(self.screen)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)

        font = pygame.font.SysFont('comicsans', 30)
        text = font.render('Score: %d' % self.score, True, (255,255,255))
        self.screen.blit(text, (10,10))
        pygame.display.flip()

class Player():
    def __init__(self, x, y, size, color, speed):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = speed

    def draw(self, screen):
        #pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self):
        key = pygame.key.get_pressed()
        if self.x > 0:
            if key[pygame.K_LEFT]:
                self.x -= self.speed
        if self.x < 800:
            if key[pygame.K_RIGHT]:
                self.x += self.speed
        if self.y > 0:
            if key[pygame.K_UP]:
                self.y -= self.speed
        if self.y < 600:
            if key[pygame.K_DOWN]:
                self.y += self.speed


class Enemy():
    def __init__(self, size, color):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.size = size
        self.color = color
        self.speed = random.randint(2, 10)
        self.direction = random.choice([-1, 1])

    def move(self):
        self.y += self.speed * self.direction
        if self.y > 600 or self.y < 0:
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])

class Price():
    def __init__(self, color):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)
        self.size = 20
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def move(self):
        self.x = random.randint(0, 800)
        self.y = random.randint(0, 600)


enemies = [Enemy(20, (255, 0,0)) for _ in range(10)]
player = Player(20, 580, 20, (255, 255,255), 5)
price = Price((255,255,0))
game = Game(800, 600, player, enemies, price)
game.run()
