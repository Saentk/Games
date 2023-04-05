from road import Road
import pygame as p
import sys

def check_events(dragon): 
    for event in p.event.get(): 
        if event.type == p.QUIT: 
            sys.exit() 
        elif event.type == p.KEYDOWN: 
            check_keydown_events(event, dragon)

def check_keydown_events(event, dragon):
    if event.key == p.K_SPACE:
        dragon.jump_flag = True


def create_rocks(game_settings, screen, rocks):
    for i in range(10):
        rock = Road(game_settings, screen)
        rocks.add(rock)

def update_road(rocks, obsticle, dragon, score):
    for rock in rocks.sprites():
        rock.update()
    obsticle.update(score)
    check_collide(dragon, obsticle, score)
    score.show_score()

def check_collide(dragon, obsticle, score):
    if obsticle.rect.colliderect(dragon):
        score.reset_stats()
        p.time.wait(1000)
        obsticle.rect.x = 900
        score.prep_score()

def update_screen(game_settings, screen, surf):
    screen.fill(game_settings.color)
    screen.blit(surf.image, surf.rect)