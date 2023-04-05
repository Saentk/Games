import pygame as p
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from start_button import Button
from score import Score

def run_game():
	p.init()
	game_settings = Settings()
	screen = p.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	p.display.set_caption('Invasion')
	ship = Ship(game_settings, screen)
	stars, drops = Group(), Group()
	bullets, aliens = Group(), Group()
	score = Score(game_settings, screen)
	
	gf.create_fleet(game_settings, screen, ship, aliens)
	gf.create_stars(game_settings, screen, stars)
	gf.create_drops(game_settings, screen, drops)

	play_button = Button(game_settings, screen, 'Play')

	while True:
		gf.check_events(game_settings, screen, play_button, ship, bullets)
		if game_settings.game_active:
			ship.update()
			gf.update_bullets(game_settings, screen, ship, aliens, bullets, score)
			gf.update_aliens(game_settings, screen, ship, aliens, bullets)
		gf.update_screen(game_settings, screen, ship, aliens, bullets, play_button, score, drops, stars)

run_game()

