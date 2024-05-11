import pygame
import time
import random
import sys

SCREEN_WIDTH: int = 780
SCREEN_HEIGHT: int = 520
IMAGES_PATH = 'images/'
FPS: int = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


class Player:
    pass


class Game:
    bg_image = None
    game_run: bool = False

    def __init__(self):
        self.bg_x: int = 0
        self.bg_y: int = -SCREEN_HEIGHT
        self.bg_y_speed: float = 0.2
        self.bg_y_pos = self.bg_y
        self.bg_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT * 2))

        self.interval = time.time()
        self.dt = 1

    def delta_time(self):
        clock.tick(FPS)
        self.dt = time.time() - self.interval
        self.interval = time.time()

    def add_background(self):
        self.bg_image = pygame.image.load(IMAGES_PATH + 'bg02.png')
        nx = int(SCREEN_WIDTH / self.bg_image.get_width())
        ny = int(SCREEN_HEIGHT / self.bg_image.get_height())
        w = self.bg_image.get_width()
        h = self.bg_image.get_height()

        for x in range(nx):
            for y in range(ny * 2):
                self.bg_surface.blit(self.bg_image, (w * x, h * y))

    def draw_background(self):
        self.bg_y_pos += self.bg_y_speed
        self.bg_y = int(self.bg_y_pos)

        if self.bg_y >= 0:
            self.bg_y = -SCREEN_HEIGHT
            self.bg_y_pos = self.bg_y

        screen.blit(self.bg_surface, (self.bg_x, self.bg_y))

    def menu(self):
        im = pygame.image.load(IMAGES_PATH + 'bg_menu.jpg')
        screen.blit(im, (0, 0))
        font = pygame.font.SysFont('Calibri', 35)
        mes = 's'
        text = font.render(mes, True, 'White')
        screen.blit(text, (300, 120))

    def init(self):
        while True:
            self.delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.run()

            self.menu()
            pygame.display.update()

    def run(self):
        self.game_run = True
        self.add_background()

        while self.game_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.game_run = False

            self.draw_background()
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.init()
