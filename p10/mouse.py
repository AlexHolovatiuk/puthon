import pygame
import sys

pygame.init()
resolution = (600, 400)
screen = pygame.display.set_mode(resolution)

def draw_circle(action):
    if action == 'paint':
        color = (255, 0, 50)
    elif action == 'clear':
        color = (0, 0, 0)

    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, color, mouse_pos, 20)
    pygame.display.update()

def main():
    is_button_action = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_button_action = 'paint'
                if event.button == 3:
                    is_button_action = 'clear'
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    is_button_action = ''

        if is_button_action:
            draw_circle(is_button_action)

    sys.exit()



main()