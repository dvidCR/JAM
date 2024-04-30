import pygame
from Level import Level

pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 960

worldx = 800
worldy = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

player_x = 400
player_y = 300
player_speed = 5

# Definir la posición de la cámara
camera_x = 0
camera_y = 0

# defino el tamaño de los 
gloc = []
tx = 64
ty = 64

i = 0
while i <= (worldx / tx) + tx:
    gloc.append(i * tx)
    i = i + 1

ground_list = Level.ground(1, gloc, tx, ty)
#plat_list = Level.platform(1, tx, ty)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    camera_x = player_x - SCREEN_WIDTH / 2
    camera_y = player_y - SCREEN_HEIGHT / 2

    keys = pygame.key.get_pressed()

    # Mover el personaje
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, (255, 0, 0), (int(player_x - camera_x), int(player_y - camera_y)), 20)
    
    ground_list.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()