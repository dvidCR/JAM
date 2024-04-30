import pygame
import sys

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Definir la posición de la cámara
camera_x = 0
camera_y = 0

menu = True

#menu
font = pygame.font.Font(None, 36)
menu_options = ["Jugar", "Configuración", "Salir"]
selected_option = 0

# Cargar la canción del menú
pygame.mixer.init()
menu_music = pygame.mixer.Sound("./Music/mayonnaise on an escalator.mp3")

def draw_menu():
    screen.fill((0,0,0))
    for i, option in enumerate(menu_options):
        text_surface = font.render(option, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, 200 + i * 50))
        screen.blit(text_surface, text_rect)

        if i == selected_option:
            pygame.draw.rect(screen, (255, 255, 255), text_rect, 2)
            
def play():
    menu_music.stop()
    player_x = 400
    player_y = 300
    player_speed = 5
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
    
    pygame.draw.circle(screen, (255, 0, 0), (int(player_x - camera_x), int(player_y - camera_y)), 20)

# Iniciar la música del menú
menu_music.play(-1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if menu:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:
                        print("Iniciar juego")
                        menu = False
                    elif selected_option == 1:
                        print("Abrir configuración")
                        menu = False
                        # Aquí puedes agregar la lógica para abrir la configuración
                    elif selected_option == 2:
                        print("Salir del juego")
                        pygame.quit()
                        sys.exit()
            else:
                if event.key == pygame.K_ESCAPE:  # Volver al menú cuando se presiona la tecla ESC
                    menu = True
                    # Reiniciar la reproducción de la música del menú cuando vuelvas al menú
                    menu_music.play(-1)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((128, 0, 128))  # purple

    if menu:
        draw_menu()
    else:
        play()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(90)  # limits FPS to 120

pygame.quit()
