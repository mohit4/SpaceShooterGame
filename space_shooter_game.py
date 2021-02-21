from math import ceil
import random
import time

import pygame as pg
from pygame.locals import QUIT
from pygame.locals import KEYDOWN
from pygame.locals import K_ESCAPE
from pygame.locals import K_SPACE
from pygame.locals import RLEACCEL

from sounds import SPACE_SHOOTER_GAME_MUSIC_PATH
from sounds import shooting_sound
from sounds import explosion_sound
from sprites import get_background_image
from sprites import LIFE_IMG
from Objects import Player
from Objects import PlayerLaser
from Objects import EnemyLaser
from Objects import SmallMeteor
from Objects import LargeMeteor
from Objects import EnemyShip
from Objects import EnemyUFO
from Objects import Score


def start_game():
    # Initialize PyGame
    pg.init()

    # Initialize PyGame Music
    pg.mixer.init()

    pg.mixer.music.load(SPACE_SHOOTER_GAME_MUSIC_PATH)
    pg.mixer.music.play(loops=-1)

    # Screen setup
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(pg.color.THECOLORS['black'])

    background_img = get_background_image()

    player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites = pg.sprite.Group()
    all_player_lasers = pg.sprite.Group()
    all_enemy_ships = pg.sprite.Group()
    all_enemy_lasers = pg.sprite.Group()
    all_meteors = pg.sprite.Group()

    clock = pg.time.Clock()

    ADD_ENEMY_LASER_EVENT = pg.USEREVENT + 1
    pg.time.set_timer(ADD_ENEMY_LASER_EVENT, 1000)

    ADD_SMALL_METEOR_EVENT = pg.USEREVENT + 2
    pg.time.set_timer(ADD_SMALL_METEOR_EVENT, 2000)

    ADD_LARGE_METEOR_EVENT = pg.USEREVENT + 3
    pg.time.set_timer(ADD_LARGE_METEOR_EVENT, 3000)

    ADD_ENEMY_SHIP_EVENT = pg.USEREVENT + 4
    pg.time.set_timer(ADD_ENEMY_SHIP_EVENT, 3000)

    ADD_ENEMY_UFO_EVENT = pg.USEREVENT + 5
    pg.time.set_timer(ADD_ENEMY_UFO_EVENT, 60000)

    game_life = pg.image.load(LIFE_IMG).convert()
    game_life.set_colorkey(pg.color.THECOLORS['black'], RLEACCEL)

    player_life = 3

    score = Score(SCREEN_WIDTH)

    running = True
    while running:

        if player_life == 0:
            running = False

        for event in pg.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADD_SMALL_METEOR_EVENT:
                x = random.randint(0, SCREEN_WIDTH)
                y = -30
                small_meteor = SmallMeteor(x, y)
                all_meteors.add(small_meteor)
                all_sprites.add(small_meteor)
            elif event.type == ADD_LARGE_METEOR_EVENT:
                x = random.randint(0, SCREEN_WIDTH)
                y = -30
                large_meteor = LargeMeteor(x, y)
                all_meteors.add(large_meteor)
                all_sprites.add(large_meteor)
            elif event.type == ADD_ENEMY_SHIP_EVENT:
                x = random.randint(0, SCREEN_WIDTH)
                y = -30
                enemy_ship = EnemyShip(x, y)
                all_enemy_ships.add(enemy_ship)
                all_sprites.add(enemy_ship)
            elif event.type == ADD_ENEMY_UFO_EVENT:
                x = -30
                y = random.randint(0, ceil(SCREEN_HEIGHT / 2))
                enemy_ufo = EnemyUFO(x, y)
                all_enemy_ships.add(enemy_ufo)
                all_sprites.add(enemy_ufo)
            elif event.type == ADD_ENEMY_LASER_EVENT:
                for enemy_ship in all_enemy_ships:
                    if not enemy_ship.enemy_fired:
                        enemy_laser = EnemyLaser(enemy_ship.x, enemy_ship.y)
                        all_enemy_lasers.add(enemy_laser)
                        all_sprites.add(enemy_laser)
                        shooting_sound.play()

        pressed_keys = pg.key.get_pressed()

        no_of_objects_in_row = ceil(SCREEN_WIDTH / background_img.get_width())
        no_of_objects_in_column = ceil(SCREEN_HEIGHT / background_img.get_height())

        for i in range(no_of_objects_in_row):
            for j in range(no_of_objects_in_column):
                rect = background_img.get_rect()
                rect.topleft = (
                    i * background_img.get_width(),
                    j * background_img.get_height()
                )
                screen.blit(background_img, rect)

        screen.blit(background_img, background_img.get_rect())

        screen.blit(player.surf, player.rect)

        if pressed_keys[K_SPACE]:
            if not player.player_fired:
                shooting_sound.play()
                laser = PlayerLaser(player.x, player.rect.top)
                all_player_lasers.add(laser)
                all_sprites.add(laser)
                player.player_fire()

        for sprite in all_sprites:
            sprite.update()
            screen.blit(sprite.surf, sprite.rect)

        score.update()
        player.update(pressed_keys)

        for player_laser in all_player_lasers:
            meteor_hit = pg.sprite.spritecollideany(player_laser, all_meteors)
            ship_hit = pg.sprite.spritecollideany(player_laser, all_enemy_ships)
            if meteor_hit is not None:
                meteor_hit.kill()
                player_laser.kill()
                explosion_sound.play()
                if type(meteor_hit) == SmallMeteor:
                    score.add_to_score(100)
                else:
                    score.add_to_score(50)
            if ship_hit is not None:
                ship_hit.kill()
                player_laser.kill()
                explosion_sound.play()
                if type(ship_hit) == EnemyUFO:
                    score.add_to_score(1000)
                    player_life += 1
                else:
                    score.add_to_score(150)

        if pg.sprite.spritecollideany(player, all_meteors) or pg.sprite.spritecollideany(player,
                                                                                         all_enemy_ships) or pg.sprite.spritecollideany(
                player, all_enemy_lasers):
            player.kill()
            explosion_sound.play()
            time.sleep(1)
            for sprite in all_sprites:
                sprite.kill()
            player_life -= 1

        for i in range(player_life):
            screen.blit(game_life, game_life.get_rect(
                center=(
                    i * game_life.get_width() + game_life.get_width(),
                    game_life.get_height()
                )
            ))

        screen.blit(score.score_text, score.rect)

        pg.display.flip()

        clock.tick(30)


pg.mixer.quit()
pg.quit()
