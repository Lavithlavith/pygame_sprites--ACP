import pygame
pygame.init()


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption(" Rectangle Game")


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)



player = pygame.Rect(50, 50, 50, 50)
second = pygame.Rect(200, 150, 50, 50)


speed = 0.7

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, player)
        pygame.draw.rect(screen, BLUE, second)
        pygame.display.flip()


pygame.quit()
