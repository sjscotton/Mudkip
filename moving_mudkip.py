import pygame
from pygame.sprite import Group

from mudkip import Mudkip
from settings import Settings
import game_functions as gf
from berry import Berry
from pygame.sprite import Group
from pygame.locals import *



def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Mudkip")

    mudkip = Mudkip(ai_settings, screen)
    rain = Group()
    berries = Group()
    animated_berries = Group()
    # gf.add_rain(ai_settings, screen, rain)
    pygame.time.set_timer(USEREVENT+1, 1000)
    # gf.add_berry(ai_settings, screen, berries)
    # berry = Berry(ai_settings, screen)
    # berries.add(berry)
    # berry.blitme()


    while True:

        gf.check_for_berries(ai_settings, screen, berries)
        gf.check_mudkip_berry_collisions(ai_settings, screen, mudkip, berries, animated_berries)
        gf.check_events(ai_settings, screen, rain, mudkip)
        mudkip.update()
        gf.update_screen(ai_settings, screen, mudkip, berries, rain, animated_berries)
    pygame.quit()
run_game()

