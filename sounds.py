import os

import pygame as pg

pg.mixer.init()

SOUNDS_DIR = os.path.join("resources", "sounds")
MUSIC_DIR = os.path.join("resources", "music")

SPACE_SHOOTER_GAME_MUSIC_FILE_NAME = "laser_show_background.wav"
SPACE_SHOOTER_GAME_MUSIC_PATH = os.path.join(MUSIC_DIR, SPACE_SHOOTER_GAME_MUSIC_FILE_NAME)

EXPLOSION_SOUND_FILE_NAME = "explosion.mp3"
EXPLOSION_SOUND_PATH = os.path.join(SOUNDS_DIR, EXPLOSION_SOUND_FILE_NAME)

LASER_SHOT_FILE_NAME = "laser_shot.wav"
LASER_SHOT_PATH = os.path.join(SOUNDS_DIR, LASER_SHOT_FILE_NAME)

shooting_sound = pg.mixer.Sound(LASER_SHOT_PATH)
explosion_sound = pg.mixer.Sound(EXPLOSION_SOUND_PATH)
