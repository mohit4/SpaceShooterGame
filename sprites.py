import os

import pygame as pg
pg.init()

SPRITES_DIR = os.path.join("resources", "sprites")
BACKGROUND_DIR = os.path.join(SPRITES_DIR, "backgrounds")
PLAYER_DIR = os.path.join(SPRITES_DIR, "player")
EFFECTS_DIR = os.path.join(SPRITES_DIR, "effects")
OBJECTS_DIR = os.path.join(SPRITES_DIR, "objects")

STAR_BACKGROUND_IMG_PATH = os.path.join(BACKGROUND_DIR, "starBackground.png")

PLAYER_IMG_CENTER = os.path.join(PLAYER_DIR, "player.png")
PLAYER_IMG_LEFT = os.path.join(PLAYER_DIR, "playerLeft.png")
PLAYER_IMG_RIGHT = os.path.join(PLAYER_DIR, "playerRight.png")
PLAYER_IMG_DAMAGED = os.path.join(PLAYER_DIR, "playerDamaged.png")

PLAYER_LASER_IMG_PATH = os.path.join(EFFECTS_DIR, "laserGreen.png")
ENEMY_LASER_IMG_PATH = os.path.join(EFFECTS_DIR, "laserRed.png")

PLAYER_LASER_HIT_IMG = os.path.join(EFFECTS_DIR, "laserGreenShot.png")
ENEMY_LASER_HIT_IMG = os.path.join(EFFECTS_DIR, "laserRedShot.png")

SMALL_STAR_IMG = os.path.join(EFFECTS_DIR, "starSmall.png")
BIG_STAR_IMG = os.path.join(EFFECTS_DIR, "starBig.png")

EXPLOSION_IMG_1 = os.path.join(EFFECTS_DIR, "Explosion_1.png")
EXPLOSION_IMG_2 = os.path.join(EFFECTS_DIR, "Explosion_2.png")
EXPLOSION_IMG_3 = os.path.join(EFFECTS_DIR, "Explosion_3.png")
EXPLOSION_IMG_4 = os.path.join(EFFECTS_DIR, "Explosion_4.png")
EXPLOSION_IMG_5 = os.path.join(EFFECTS_DIR, "Explosion_5.png")
EXPLOSION_IMG_6 = os.path.join(EFFECTS_DIR, "Explosion_6.png")
EXPLOSION_IMG_7 = os.path.join(EFFECTS_DIR, "Explosion_7.png")

EXPLOSION_SEQ = [
    EXPLOSION_IMG_1,
    EXPLOSION_IMG_2,
    EXPLOSION_IMG_3,
    EXPLOSION_IMG_4,
    EXPLOSION_IMG_5,
    EXPLOSION_IMG_6,
    EXPLOSION_IMG_7
]

SMALL_METEOR_IMG = os.path.join(OBJECTS_DIR, "meteorSmall.png")
LARGE_METEOR_IMG = os.path.join(OBJECTS_DIR, "meteorBig.png")
SPEED_LINE_IMG = os.path.join(EFFECTS_DIR, "speedLine.png")

ENEMY_SHIP_IMG = os.path.join(OBJECTS_DIR, "enemyShip.png")

UFO_IMG = os.path.join(OBJECTS_DIR, "enemyUFO.png")

LIFE_IMG = os.path.join(OBJECTS_DIR, "life.png")


def get_background_image():
    return pg.image.load(STAR_BACKGROUND_IMG_PATH).convert()
