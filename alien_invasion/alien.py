import pygame as p 
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, game_settings, screen):
		Sprite.__init__(self)
		self.screen = screen
		self.game_settings = game_settings

		self.image = p.image.load('images/ufo.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def update(self):
		self.x += (self.game_settings.alien_speed_factor * self.game_settings.fleet_direction)
		self.rect.x = self.x

	def check_edges(self):
		if self.rect.right >= self.game_settings.screen_width:
			return True
		if self.rect.left <= 0:
			return True

