import pygame

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

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player = Player(400, 300, 50, (35, 255, 150))
player.draw()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    screen.fill((255,255,5))
    player.move()
    player.draw()

    pygame.display.flip()
    clock.tick(60)