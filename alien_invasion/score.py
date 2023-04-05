import pygame as p

class Score:
	def __init__(self, game_settings, screen):
		self.screen = screen
		self.game_settings = game_settings

		self.text_color = (30, 30, 30)
		self.font = p.font.SysFont(None, 48)

		self.reset_stats()
		self.prep_score()

	def prep_score(self):
		score_str = str(self.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.bg_color)
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.game_settings.screen_width - 20
		self.score_rect.top = 20

	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)

	def reset_stats(self):
		self.score = 0