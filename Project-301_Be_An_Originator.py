import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))

running  = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    color = (255, 255, 255)

    #S
    rectangle1 = pygame.Rect(20, 150, 70, 10)
    pygame.draw.rect(screen, color, rectangle1)

    rectangle2 = pygame.Rect(20, 150, 10, 50)
    pygame.draw.rect(screen, color, rectangle2)

    rectangle3 = pygame.Rect(20, 200, 70, 10)
    pygame.draw.rect(screen, color, rectangle3)

    rectangle4 = pygame.Rect(90, 200, 10, 50) 
    pygame.draw.rect(screen, color, rectangle4)

    rectangle5 = pygame.Rect(20, 250, 80, 10)
    pygame.draw.rect(screen, color, rectangle5)

    #E
    pygame.draw.line(screen, color, (130, 150), (200, 150), 10)

    pygame.draw.line(screen, color, (135, 150), (135, 260), 10)

    pygame.draw.line(screen, color, (135, 205), (200, 205), 10)

    pygame.draw.line(screen, color, (135, 260), (200, 260), 10)

    #A
    pygame.draw.line(screen, color, (250, 150), (220, 260), 10)
    
    pygame.draw.line(screen, color, (250, 150), (280, 260), 10)

    pygame.draw.line(screen, color, (230, 205), (260, 205), 10)

    #N
    pygame.draw.line(screen, color, (300, 150), (300, 260), 10)

    pygame.draw.line(screen, color, (300, 150), (360, 260), 10)

    pygame.draw.line(screen, color, (360, 260), (360, 150), 10)

    pygame.display.flip()

pygame.quit()