from pico2d import *
import game_world
import game_framework

class Bird:
    def __init__(self, x = 400 , y = 500):
        self.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.flip = ''

    def draw(self):
        self.image.clip_composite_draw((self.frame % 5) * 183, (2 - (self.frame // 5)) * 168, 180, 168, 0, self.flip, self.x, self.y, 100, 100)

    def update(self):
        self.frame = (self.frame + 1) % 14
        if self.x > 1600:
            self.dir = -1
            self.flip = 'h'
        elif self.x < 0:
            self.dir = 1
            self.flip = ''
        delay(0.1)
