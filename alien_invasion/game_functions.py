import sys, random, time
import pygame as p
from ship import Bullet
from alien import Alien
from other import Star, Drop


def check_keydown_events(event, game_settings, screen, ship, bullets): 
    if event.key == p.K_RIGHT: 
        ship.moving_right = True 
    elif event.key == p.K_LEFT: 
        ship.moving_left = True 
    elif event.key == p.K_SPACE:
        fire_bullets(game_settings, screen, ship, bullets)
    elif event.key == p.K_q: 
        sys.exit()
    elif event.key == p.K_RETURN:
        game_settings.game_active = True
        ship.ships_left = game_settings.lifes


def check_keyup_events(event, ship): 
    if event.key == p.K_RIGHT: 
        ship.moving_right = False 
    elif event.key == p.K_LEFT: 
        ship.moving_left = False 


def check_events(game_settings, screen, play_button, ship, bullets): 
    for event in p.event.get(): 
        if event.type == p.QUIT: 
            sys.exit() 
        elif event.type == p.KEYDOWN: 
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == p.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == p.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = p.mouse.get_pos()
            check_play_button(game_settings, play_button, ship, mouse_x, mouse_y)


def check_play_button(game_settings, play_button, ship, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game_settings.game_active = True


def update_screen(game_settings, screen, ship, aliens, bullets, play_button, score, drops, stars):
    screen.fill(game_settings.bg_color)
    update_decorations(game_settings, screen, drops, stars)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    ship.blitme()
    if game_settings.game_active == False:
        play_button.draw_button()
    score.show_score()
    p.display.flip()


def update_bullets(game_settings, screen, ship, aliens, bullets, score):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collisions(game_settings, screen, ship, aliens, bullets, score)


def check_collisions(game_settings, screen, ship, aliens, bullets, score):
    collisions = p.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for alien in collisions:
            score.score += game_settings.alien_points
            score.prep_score()
    if len(aliens) == 0:
        create_fleet(game_settings, screen, ship, aliens)
        game_settings.fleet_drop_speed += 5


def fire_bullets(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x 
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for  alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)


def get_number_rows(game_settings, ship_height, alien_height):
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    rows_number = int(available_space_y / (2 * alien_height))
    return rows_number


def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break


def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1


def update_aliens(game_settings, screen, ship, aliens, bullets):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if p.sprite.spritecollideany(ship, aliens):
        lose_life(game_settings, screen, ship, aliens, bullets)
    check_aliens_bottom(game_settings, screen, ship, aliens, bullets)      


def lose_life(game_settings, screen, ship, aliens, bullets):
    ship.ships_left -= 1
    print(ship.ships_left)
    if ship.ships_left == 0:
        game_settings.game_active = False
    
    bullets.empty()
    aliens.empty()

    create_fleet(game_settings, screen, ship, aliens)
    ship.back_to_center()
    time.sleep(0.5)


def check_aliens_bottom(game_settings, screen, ship, aliens, bullets):
    for alien in aliens.sprites():
        if alien.rect.bottom >= game_settings.screen_height:
            lose_life(game_settings, screen, ship, aliens, bullets)
            break


def create_stars(game_settings, screen, stars):
    for x in range(random.randint(40, 60)):
        star = Star()
        star.rect.y = random.randint(0, game_settings.screen_height)
        star.rect.x = random.randint(0, game_settings.screen_width)
        stars.add(star)


def create_drops(game_settings, screen, drops):
    for x in range(20):
        drop = Drop()
        drop.rect.x = random.randint(0, game_settings.screen_width)
        drop.rect.y = random.randint(0, game_settings.screen_height)
        drops.add(drop)


def update_drops(game_settings ,drops):
    for drop in drops.sprites():
        drop.rect.y += 1
        if drop.rect.y >= game_settings.screen_height:
            drop.rect.y = 1
            drop.rect.x = random.randint(0, game_settings.screen_width)


def update_decorations(game_settings, screen, drops, stars):
    drops.draw(screen)
    stars.draw(screen)
    update_drops(game_settings, drops)

