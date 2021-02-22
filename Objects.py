import random

import pygame as pg
from pygame.locals import RLEACCEL
from pygame.locals import K_LEFT
from pygame.locals import K_RIGHT
from pygame.locals import K_UP
from pygame.locals import K_DOWN
from pygame.locals import K_SPACE

from sprites import PLAYER_IMG_CENTER
from sprites import PLAYER_IMG_LEFT
from sprites import PLAYER_IMG_RIGHT
from sprites import PLAYER_IMG_DAMAGED
from sprites import PLAYER_LASER_IMG_PATH
from sprites import ENEMY_LASER_IMG_PATH
from sprites import SMALL_METEOR_IMG
from sprites import LARGE_METEOR_IMG
from sprites import ENEMY_SHIP_IMG
from sprites import UFO_IMG
from sprites import EXPLOSION_SEQ
from sprites import SMALL_STAR_IMG
from sprites import BIG_STAR_IMG
from sprites import SPEED_LINE_IMG
from fonts import get_text


class SmallMeteor(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(SmallMeteor, self).__init__()
        self.speed = 15
        self.x = x
        self.y = y
        self.surf = pg.image.load(SMALL_METEOR_IMG).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += self.speed
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.y > 1000:
            self.kill()


class LargeMeteor(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(LargeMeteor, self).__init__()
        self.speed = 2
        self.x = x
        self.y = y
        self.surf = pg.image.load(LARGE_METEOR_IMG).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += self.speed
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.y > 1000:
            self.kill()


class EnemyUFO(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(EnemyUFO, self).__init__()
        self.speed = 5
        self.x = x
        self.y = y
        self.enemy_fired = False
        self.enemy_fired_delay = 0
        self.surf = pg.image.load(UFO_IMG).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def enemy_fire(self):
        self.enemy_fired = True
        self.enemy_fired_delay = 10

    def update(self):
        self.x += self.speed
        self.y += random.choice([x for x in range(-2 * self.speed, 2 * self.speed)])
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.x > 1500:
            self.kill()

        if self.enemy_fired:
            self.enemy_fired_delay -= 1
            if self.enemy_fired_delay <= 0:
                self.enemy_fired = False


class EnemyShip(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(EnemyShip, self).__init__()
        self.speed = 5
        self.x = x
        self.y = y
        self.enemy_fired = False
        self.enemy_fired_delay = 0
        self.surf = pg.image.load(ENEMY_SHIP_IMG).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def enemy_fire(self):
        self.enemy_fired = True
        self.enemy_fired_delay = 10

    def update(self):
        self.y += self.speed
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.y > 1000:
            self.kill()

        if self.enemy_fired:
            self.enemy_fired_delay -= 1
            if self.enemy_fired_delay <= 0:
                self.enemy_fired = False


class EnemyLaser(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(EnemyLaser, self).__init__()
        self.speed = 10
        self.x = x
        self.y = y
        self.surf = pg.image.load(ENEMY_LASER_IMG_PATH).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += self.speed
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.y > 1000:
            self.kill()


class PlayerLaser(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(PlayerLaser, self).__init__()
        self.speed = 15
        self.x = x
        self.y = y
        self.surf = pg.image.load(PLAYER_LASER_IMG_PATH).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y -= self.speed
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )
        if self.y < 0:
            self.kill()


class SmallStar(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(SmallStar, self).__init__()

        self.x = random.randint(0, screen_width)
        self.y = -30

        self.surf = pg.image.load(SMALL_STAR_IMG).convert()
        self.surf.set_alpha(128)
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += 10
        self.rect.center = (self.x, self.y)
        if self.y > 1000:
            self.kill()


class BigStar(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(BigStar, self).__init__()

        self.x = random.randint(0, screen_width)
        self.y = -30

        self.surf = pg.image.load(BIG_STAR_IMG).convert()
        self.surf.set_alpha(128)
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += 5
        self.rect.center = (self.x, self.y)
        if self.y > 1000:
            self.kill()


class SpeedLine(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(SpeedLine, self).__init__()

        self.x = random.randint(0, screen_width)
        self.y = -30

        self.surf = pg.image.load(SPEED_LINE_IMG).convert()
        self.surf.set_alpha(10)
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)

        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.y += 30
        self.rect.center = (self.x, self.y)
        if self.y > 1000:
            self.kill()


class Player(pg.sprite.Sprite):

    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()

        self.horizontal_limit = screen_width
        self.vertical_limit = screen_height

        self.speed_x = 15
        self.speed_y = 10

        self.player_fired = False
        self.player_fired_delay = 0

        self.surf = pg.image.load(PLAYER_IMG_CENTER).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)

        self.x = (screen_width - self.surf.get_width()) / 2
        self.y = (screen_height - 5 - self.surf.get_height() / 2)

        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def player_fire(self):
        self.player_fired = True
        self.player_fired_delay = 10

    def update(self, pressed_keys):

        if pressed_keys[K_LEFT]:
            self.x -= self.speed_x
            self.surf = pg.image.load(PLAYER_IMG_LEFT).convert()
        elif pressed_keys[K_RIGHT]:
            self.x += self.speed_x
            self.surf = pg.image.load(PLAYER_IMG_RIGHT).convert()
        elif pressed_keys[K_UP]:
            self.y -= self.speed_y
            self.surf = pg.image.load(PLAYER_IMG_CENTER).convert()
        elif pressed_keys[K_DOWN]:
            self.y += self.speed_y
            self.surf = pg.image.load(PLAYER_IMG_CENTER).convert()
        else:
            self.surf = pg.image.load(PLAYER_IMG_CENTER).convert()

        self.surf.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

        if self.rect.right > self.horizontal_limit:
            self.x = self.horizontal_limit - (self.rect.width / 2)
        if self.rect.left < 0:
            self.x = self.rect.width / 2

        if self.rect.top < self.vertical_limit * 0.66:
            self.y = self.vertical_limit * 0.66 + self.rect.height / 2
        if self.rect.bottom > self.vertical_limit:
            self.y = self.vertical_limit - (self.rect.height / 2)

        if self.player_fired:
            self.player_fired_delay -= 1
            if self.player_fired_delay <= 0:
                self.player_fired = False


class Score(pg.sprite.Sprite):

    def __init__(self, screen_width):
        super(Score, self).__init__()

        self.x = screen_width / 2
        self.y = 20

        self.score = 0
        self.score_text = get_text(str(self.score))
        self.score_text.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.score_text.get_rect(
            center=(self.x, self.y)
        )

    def add_to_score(self, count):
        self.score += count

    def update(self):
        self.score_text = get_text(str(self.score))
        self.score_text.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)
        self.rect = self.score_text.get_rect(
            center=(self.x, self.y)
        )


class State:

    def __init__(self, animation_seq):
        self.animation_seq = animation_seq
        self.animation_seq_index = 0
        self.is_completed = False

    def get_current_image(self):
        if not self.is_completed:
            return self.animation_seq[self.animation_seq_index]
        return None

    def update(self):
        self.animation_seq_index += 1
        if self.animation_seq_index >= len(self.animation_seq):
            self.is_completed = True


class Explosion(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(Explosion, self).__init__()
        self.x = x
        self.y = y

        self.state = State(EXPLOSION_SEQ)

        self.surf = pg.image.load(self.state.get_current_image()).convert()
        self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(self.x, self.y)
        )

    def update(self):
        self.state.update()
        current_image = self.state.get_current_image()
        if current_image is None:
            self.kill()
        else:
            self.surf = pg.image.load(current_image).convert()
            self.surf.set_colorkey(pg.color.THECOLORS['white'], RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(self.x, self.y)
            )
