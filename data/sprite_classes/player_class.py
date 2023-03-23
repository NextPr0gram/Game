import pygame
from sprite_classes.entity_class import Entity
from configs import config


class Player(Entity):
    def __init__(self, pos_x, pos_y, width, height, sprite_group) -> None:
        super().__init__(pos_x, pos_y, width, height, sprite_group)

    def update(self):
        super().update()
        # Check for keyboard input
        keys = pygame.key.get_pressed()
        if keys[config.move_left]:
            self.move_left()
        if keys[config.move_right]:
            self.move_right()
        if keys[config.move_up]:
            self.move_up()
        if keys[config.move_down]:
            self.move_down()
