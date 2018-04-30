import pygame
from pygame.sprite import Group

from mudkip import Mudkip
from settings import Settings
import game_functions as gf
from berry import Berry
from pygame.sprite import Group



def run_game():
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Mudkip")

    mudkip = Mudkip(ai_settings, screen)

    berries = Group()
    # gf.add_berry(ai_settings, screen, berries)
    # berry = Berry(ai_settings, screen)
    # berries.add(berry)
    # berry.blitme()


    while True:

        gf.check_for_berries(ai_settings, screen, berries)
        gf.check_mudkip_berry_collisions(ai_settings, screen, mudkip, berries)
        gf.check_events(mudkip)
        mudkip.update()
        gf.update_screen(ai_settings, screen, mudkip, berries)
    pygame.quit()
run_game()

