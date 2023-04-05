import pygame as p
from random import randint, choice
from pygame.sprite import Sprite

class Road(Sprite):
    def __init__(self, game_settings, screen):
        Sprite.__init__(self)
        self.game_settings = game_settings
        self.screen = screen

        self.x = float(randint(10, game_settings.width))
        self.y = 370 - randint(1,10)

    def draw(self):
        p.draw.circle(self.screen, (0,0,0), (self.x, self.y), 3, 2)

    def update(self):
        self.x -= 0.5
        if self.x == 0:
            self.x = self.game_settings.width + randint(1, 20)
            self.y = 370 - randint(1,5)
        self.draw()

class Surface:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.image = p.image.load("img\\road.jpg")
        self.rect = self.image.get_rect()
        self.rect.bottom = game_settings.height


class Obsticle:
    def __init__(self, game_settings, screen):
        self.game_settings = game_settings
        self.screen = screen

        self.list_of_images = ["img\\tree.png", "img\\tree1.png", "img\\tree2.png", "img\\landslide.png", "img\\rocks.png"]
        self.images = []
        self.load_images()

        self.image = choice(self.images)

        self.rect = self.image.get_rect()
        self.rect.bottom = 370

        self.rect.x = 700

    def load_images(self):
        for image in self.list_of_images:
            image = p.image.load(image)
            image = p.transform.scale(image, (100, 100))
            self.images.append(image)

    def check_rect(self, score):
        if self.rect.x <= -500:
            self.rect.x = 800
            self.image = choice(self.images)
            score.score += 10
            score.prep_score()


    def update(self, score):
        self.rect.x -= 1
        self.check_rect(score)
        self.draw()

    def draw(self):
        self.screen.blit(self.image, self.rect)