import pygame as p 
from pygame.sprite import Sprite

class Star(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = p.image.load('images/star.bmp')
		self.rect = self.image.get_rect()

class Drop(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		self.image = p.image.load('images/drop.bmp')
		self.rect = self.image.get_rect()


