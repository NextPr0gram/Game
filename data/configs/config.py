import configparser, os

configparser = configparser.RawConfigParser()
keybinds_file_path = os.path.join(os.path.dirname(__file__), 'keybinds.cfg')
configparser.read(keybinds_file_path)

# Player movement settings(integers)
move_up = int(configparser.get("player","move_up"))
move_down = int(configparser.get("player","move_down"))
move_left = int(configparser.get("player","move_left"))
move_right = int(configparser.get("player","move_right"))
player_speed = 10


video_file_path = os.path.join(os.path.dirname(__file__), 'video.cfg')
configparser.read(video_file_path)

# Video settings

fps = 0
delta_time = 1 # Default delta time
if configparser.get("video", "fps") == "unlimited":
    fps = 0
else:
    fps = int(configparser.get("video", "fps"))



#configParser.set('info', 'Name', 'newName')
#config.write(configFilePath)