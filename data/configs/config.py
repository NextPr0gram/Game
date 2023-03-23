import pygame
import configparser
import os

configparser = configparser.RawConfigParser()
keybinds_file_path = os.path.join(os.path.dirname(__file__), 'keybinds.cfg')
configparser.read(keybinds_file_path)

# Player movement settings(integers)
move_up = int(configparser.get("player", "move_up"))
move_down = int(configparser.get("player", "move_down"))
move_left = int(configparser.get("player", "move_left"))
move_right = int(configparser.get("player", "move_right"))

# Load video.cfg
video_file_path = os.path.join(os.path.dirname(__file__), 'video.cfg')
configparser.read(video_file_path)

# Video settings
fps = 0
delta_time = 1  # Default delta time
if configparser.get("video", "fps") == "unlimited":
    fps = 0
else:
    fps = int(configparser.get("video", "fps"))

# Load textures and tile settings.cfg
video_file_path = os.path.join(os.path.dirname(__file__), 'textures.cfg')
configparser.read(video_file_path)
# Tile size
tile_size = int(configparser.get("tile_settings", "tile_size"))

# Textures locations
grass_animated_path = configparser.get("tile", "grass_animated")


# configParser.set('info', 'Name', 'newName')
# config.write(configFilePath)
