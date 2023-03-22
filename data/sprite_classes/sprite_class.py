import pygame


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height, sprite_group) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("black"))
        self.rect = self.image.get_rect()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y 
        sprite_group.add(self)

    def scale(self, multiplier):
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width()*multiplier, self.image.get_height()*multiplier))
    def update(self):
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y 
        
        
        
