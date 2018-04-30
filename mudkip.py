import pygame
from pygame.sprite import Sprite

class Mudkip(Sprite):
    def __init__(self, ai_settings, screen):
        super(Mudkip, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/mudkip.gif')
        self.image = pygame.transform.scale(self.image, ai_settings.mudkip_size)
        self.image_facing_left = self.image
        self.image_facing_right = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.mudkip_speed_factor
            self.image = self.image_facing_right
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.mudkip_speed_factor
            self.image = self.image_facing_left

        self.rect.centerx = self.centerx
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.mudkip_speed_factor
            self.image = self.image_facing_left
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.mudkip_speed_factor
            self.image = self.image_facing_right
        self.rect.centery = self.centery


    def blitme(self):
        self.screen.blit(self.image, self.rect)
