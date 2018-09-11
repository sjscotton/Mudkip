
import pygame
from pygame.sprite import Sprite
import random
from settings import Settings
import math

class Berry(Sprite):
    """one berry appears in a set amount of time, if mudkip dosent eat it in a set amount of time, more pokemon appear who want to eat it too,/ their speed increases"""
    def __init__(self, ai_settings, screen):
        super(Berry, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # self.image = pygame.image.load(random.choice(ai_settings.berry_choices))
        self.berry_type = random.randint(0, 20)

        if self.berry_type < 10:
            self.image = pygame.image.load('images/poke_razz_berry.png')
            self.berry_score = 1
        elif self.berry_type < 16:
            self.image = pygame.image.load('images/poke_orange_berry.png')
            self.berry_score = 5
        elif self.berry_type < 19:
            self.image = pygame.image.load('images/poke_nana_berry.png')
            self.berry_score = 10
        elif self.berry_type < 21:
            self.image = pygame.image.load('images/poke_pine_berry.png')
            self.berry_score = 20
        self.image = pygame.transform.scale(self.image, (ai_settings.berry_size, ai_settings.berry_size))
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(10, self.ai_settings.screen_width-10)
        self.screen_rect = screen.get_rect()
        self.rect.centery = self.screen_rect.top - 35
        self.end_position = random.randint(100, self.ai_settings.screen_height-10)
        # self.rect.centery = random.randint(100, self.ai_settings.screen_height-10)
        self.at_final_position = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def animate_in(self):
        if self.rect.centery < self.end_position:
            self.rect.centery += 1
        else:
            self.at_final_position = True

class AnimatedBerry(Sprite):

    def __init__(self, ai_settings, screen, berry):
        super(AnimatedBerry, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = berry.image
        self.rect = self.image.get_rect()

        self.rect.centerx = berry.rect.centerx
        self.rect.centery = berry.rect.centery
        self.initial_y_pos = berry.rect.centery
        self.initial_size = self.image

        self.iteration = -.50
        self.steps = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self, ai_settings):

        animation_function = ((5.9 * (self.iteration ** 2) - (self.iteration ** 3)) / 2) - 1.5
        new_berry_size = int(ai_settings.berry_size + animation_function)

        self.image = pygame.transform.scale(self.initial_size, (new_berry_size, new_berry_size))
        self.rect.centery = self.initial_y_pos - animation_function
        self.iteration += .036
        self.steps += 1