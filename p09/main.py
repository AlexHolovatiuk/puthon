# --------------------------------------------------- #
#   * * *   *   *  * * *      *     **    **  * * *   #
#   *   *    * *   *   *     * *    * *  * *  *       #
#   * * *    **    *         * *    *  *   *  * * *   #
#   *        *     *  **    * * *   *  *   *  *       #
#   *       *      * * *   *     *  *      *  * * *   #
# --------------------------------------------------- #

import pygame
import  sys

# ініціалізація бібліотеки (запустити)
pygame.init()
# створити екран
screen = pygame.display.set_mode((800, 600))
# заголовок вікная
pygame.display.set_caption('MGood-Boy')
clock = pygame.time.Clock()
clock_tick = 60

spyder_img = pygame.image.load('images/spyder.png')
spyder_position = {'x': 50, 'y': 50}


# ===================================================================
while True:
    # перевіряємо події
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        spyder_position['y'] -= 3
    if keys[pygame.K_s]:
        spyder_position['y'] += 3
    if keys[pygame.K_a]:
        spyder_position['x'] -= 3
    if keys[pygame.K_d]:
        spyder_position['x'] += 3

    screen.blit(spyder_img, (spyder_position['x'], spyder_position['y']))


    pygame.display.update()

    clock.tick(clock_tick)