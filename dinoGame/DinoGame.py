import pygame as p
from settings import Settings
import game_functions as gf
from pygame.sprite import Group
from dragon import Dragon
from road import Surface, Obsticle
from score import Score

def run_game():
    p.init()
    game_settings = Settings()
    screen = p.display.set_mode(game_settings.size)

    surf = Surface(game_settings, screen)
    dragon = Dragon(game_settings, screen)
    obsticle = Obsticle(game_settings, screen)
    rocks = Group()
    score = Score(game_settings, screen)

    gf.create_rocks(game_settings, screen, rocks)

    while True:
        gf.check_events(dragon)
        gf.update_screen(game_settings, screen, surf)
        dragon.update()
        gf.update_road(rocks, obsticle, dragon, score)
        p.display.flip()

run_game()