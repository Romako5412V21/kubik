import pygame
pygame.init()
import random

clock = pygame.time.Clock()
window = pygame.display.set_mode((1366,700))
back_color = (255, 198, 112)
game = True
player1 = pygame.Rect(680,350,50,50)
bullets = []
bullets1 = []
while game:
    clock.tick(20)
    pygame.display.update()

    window.fill(back_color)
    pygame.draw.rect(window,(103, 239, 112) ,player1)
    

    if random.randint(0,200) < 10:
        x = random.randint(0,660)
        y = -10
        bullets.append(pygame.Rect(x,y,20,20))

    for b in bullets:
        pygame.draw.rect(window, (0,0,0), b)

    for b in bullets:
        b.y += 10
        if b.colliderect(player1):
            game = False

    if random.randint(0,200) < 10:
        x = -10
        y = random.randint(0,680)
        bullets1.append(pygame.Rect(x,y,20,20))

    for b in bullets1:
        pygame.draw.rect(window, (0,0,0), b)

    for b in bullets1:
        b.x += 10
        if b.colliderect(player1):
            game = False
        

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player1.x > 0:
        player1.x -= 3
    if keys[pygame.K_d] and player1.x < 1316:
        player1.x += 3
    if keys[pygame.K_w] and player1.y > 0:
        player1.y -= 3
    if keys[pygame.K_s] and player1.y < 650:
        player1.y += 3
    
    clock.tick(20)
    pygame.display.update()
