import pygame
from sprite_classes.player_class import Player
from configs import config

# Setup pygame

pygame.init()
screen = pygame.display.set_mode([1280, 720])
clock = pygame.time.Clock()


# Setup sprites
sprite_group = pygame.sprite.Group()
player = Player(screen.get_width()/2, screen.get_height() /
                2, 50, 50, sprite_group, config.grass_animated_path)
# Tick before the next loop, used to calculate delta_time
prev_tick = pygame.time.get_ticks()
running = True
while running:
    clock.tick(config.fps)
    pygame.display.set_caption(str(clock.get_fps().__round__()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    current_tick = pygame.time.get_ticks()
    # This ensures that the sprites moves at a consistent speed that is equivalent to 60 FPS
    config.delta_time = (current_tick - prev_tick) / 1000.0 * 60
    prev_tick = current_tick

    
     
    screen.fill(pygame.Color("white"))

    sprite_group.draw(screen)
    sprite_group.update()

    pygame.display.flip()
