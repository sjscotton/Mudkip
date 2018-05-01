import pygame
from pygame.sprite import Sprite
import random

class RainDrop(Sprite):
    def __init__(self, ai_settings, screen):
        super(RainDrop, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.size = random.randint(30, 50)

        self.image = pygame.image.load('images/raindrop.png')
        self.image = pygame.transform.scale(self.image, (self.size, int(self.size*1.6)))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #self.rect.bottom = self.screen_rect.top
        self.rect.top = self.screen_rect.top
        self.rect.centerx = random.randint(0, self.ai_settings.screen_width)

    def update(self):
        self.rect.top += self.ai_settings.rain_fall_speed


    def blitme(self):
        self.screen.blit(self.image, self.rect)
