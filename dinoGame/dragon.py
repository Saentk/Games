import pygame as p

class Dragon:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.image = p.image.load('img\\dragon.png')
        self.image = p.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.bottom = 370
        self.bottom = float(self.rect.bottom)

        self.y = -0.5
        self.jump_flag = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.jump_flag:
            self.jump()
        self.blitme()
        # if self.rect.colliderect(obsticle):
        #     print('kkk')

    def check_jump(self):
        if self.bottom == 150:
            self.y *= -1
        elif self.bottom == 370:
            self.jump_flag = False
            self.y *= -1

    def jump(self):
        self.bottom += self.y
        self.check_jump()
        self.rect.bottom = self.bottom


