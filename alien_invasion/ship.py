import pygame as p
from pygame.sprite import Sprite


class Ship():
	def __init__(self, game_settings, screen):
		self.screen = screen
		self.image = p.image.load('images/ship.bmp')
		self.game_settings = game_settings
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.moving_right = False
		self.moving_left = False
		self.center = float(self.rect.centerx)

		self.ships_left = game_settings.lifes

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.game_settings.speed_factor
		self.rect.centerx = self.center

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def back_to_center(self):
		self.center = self.screen_rect.centerx

	def reset_stats(self):
		self.ships_left = self.game_settings.lifes


class Bullet(Sprite):
	def __init__(self, game_settings, screen, ship):
		Sprite.__init__(self)
		self.screen = screen

		self.rect = p.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height)

		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		self.color = game_settings.bullet_color
		self.speed_factor = game_settings.bullet_speed_factor

	def update(self):
		self.y -= self.speed_factor
		self.rect.y = self.y 

	def draw_bullet(self):
		p.draw.rect(self.screen, self.color, self.rect)