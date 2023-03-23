import pygame
from configs import config


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, sprite_group, texture_path=None) -> None:
        self.animation_frames = []
        super().__init__()
        if texture_path != None:
            self.process_sprite_sheet(texture_path)
        self.image = self.animation_frames[0]
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.frame = 0
        self.animation_counter = 0

        sprite_group.add(self)

    def scale(self, multiplier):
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width()*multiplier, self.image.get_height()*multiplier))

    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.animate()

    def process_sprite_sheet(self, texture_path):
        sprite_sheet = pygame.image.load(texture_path).convert_alpha()
        sheet_width = sprite_sheet.get_width()
        for frame in range(0, sheet_width, config.tile_size):
            image = pygame.Surface(
                (config.tile_size, config.tile_size)).convert_alpha()
            image.set_colorkey(pygame.Color("black"))
            image.blit(sprite_sheet, (0, 0), (frame, 0, frame +
                       config.tile_size, config.tile_size))
            self.animation_frames.append(image)

    def animate(self):
        if len(self.animation_frames) > 1:
            self.animation_counter += config.delta_time
            print(self.animation_counter)
            while self.animation_counter >= 15:
                self.animation_counter = 0
                self.next_frame()


    def next_frame(self):
        self.frame = (self.frame + 1) % len(self.animation_frames)
        self.image = self.animation_frames[self.frame]
