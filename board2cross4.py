import random
import arcade
import os
from model import *

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "AUTO HERO"
class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model')
    def syc_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
    def draw(self):
        self.syc_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height) 
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
 
    def update(self, delta):
        self.world.update(delta)
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()