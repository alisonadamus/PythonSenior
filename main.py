import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = screen.get_width() / 2
y = screen.get_height() / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.fill((134, 67, 90))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5


    pygame.draw.circle(screen, (255, 255, 255), (x, y), 50)


    pygame.display.flip()
    clock.tick(60)


