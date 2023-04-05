
class Settings():

	def __init__(self):
		self.screen_width = 1500
		self.screen_height = 800
		self.bg_color = (34, 168, 230)
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = 225, 0, 0
		self.fleet_direction = 1
		self.lifes = 1
		self.bullets_allowed = 3

		self.reset_settings()

	def reset_settings(self):
		self.game_active = False
		self.speed_factor = 1.5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 0.5
		self.fleet_drop_speed = 10
		self.alien_points = 50
		