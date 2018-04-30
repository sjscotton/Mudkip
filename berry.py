
import pygame
from pygame.sprite import Sprite
import random
from settings import Settings

class Berry(Sprite):
    """one berry appears in a set amount of time, if mudkip dosent eat it in a set amount of time, more pokemon appear who want to eat it too,/ their speed increases"""
    def __init__(self, ai_settings, screen):
        super(Berry, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/poke_razz_berry.png')
        self.image = pygame.transform.scale(self.image, ai_settings.berry_size)
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(10, self.ai_settings.screen_width-10)
        self.rect.centery = random.randint(10, self.ai_settings.screen_height-10)

    def blitme(self):
        self.screen.blit(self.image, self.rect)