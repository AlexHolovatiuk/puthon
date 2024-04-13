import random

class Ball:
    MAX_X = 100
    color: tuple = (0, 0, 0)
    radius: int = 0
    weight: float = 0
    speed: int = 0
    x: int = random.randint(0, MAX_X)
    y: int = 0

    def __init__(self, radius: int, weight: float):
        if radius:
            self.radius = radius
        else:
            print('Error! Radius cannot equal/less zero')

        self.weight = weight

        print('!!! Start !!!')

    def movement(self):
        self.mov_x()
        self.mov_y()

    def mov_x(self, speed_x: int = 0):
        if speed_x == 0:
            self.x += self.speed
        else:
            self.x += speed_x

    def mov_y(self, speed_x: int = 0):
        self.y += self.speed

ball_1 = Ball(12, 20)
ball_1.speed = 5

ball_1.mov_x()
ball_1.mov_x(40)
ball_1.mov_x()

print(ball_1.x, ball_1.y)


