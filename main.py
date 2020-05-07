# Initializing pygame
import pygame
pygame.init()

# Setting screen and background
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('garden1.jpg').convert()

# Caption and Icon
pygame.display.set_caption("A Day in the Garden")
icon = pygame.image.load('garden1.jpg')
# pygame.display.set_icon(icon)

# Sun
#playerImg = pygame.image.load('treeicon.png')
#playerX = 370
#playerY = 480
#playerX_change = 0



# ------ Game Loop -----------

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()