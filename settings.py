import pygame

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 130, 200)
        self.mudkip_speed_factor = 2
        self.rain_fall_speed = 1
        self.mudkip_size = (175, 175)
        self.berry_frequency = 1
        self.berry_size = (70, 70)
        self.sound_a = pygame.mixer.Sound("sound/pop.wav")