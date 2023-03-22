import pygame
from sprite_classes.sprite_class import Sprite
from configs import config


class Entity(Sprite):
    def __init__(self, pos_x, pos_y, width, height, sprite_group) -> None:
        super().__init__(pos_x, pos_y, width, height, sprite_group)
        self.speed = config.player_speed

    def move_left(self):
        self.pos_x -= self.speed * config.delta_time 

    def move_right(self):
        self.pos_x += self.speed * config.delta_time

    def move_up(self):
        self.pos_y -= self.speed * config.delta_time

    def move_down(self):
        self.pos_y += self.speed * config.delta_time

    def update(self):
        super().update()


        