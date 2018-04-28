import pygame
import sys
from mudkip import Mudkip


#
# def run_game():
#     pygame.init()
#     ai_settings = Settings()
#     screen = pygame.display.set_mode(ai_settings.screen_width. ai_settings.screen_height)
#     pygame.display.set_caption("Mudkip")
#     mudkip = Mudkip(ai_settings, screen)
#
#     while True:
#         check_events(mudkip)
#         mudkip.update()
#         update_screen(ai_settings, screen, mudkip)
#     pygame.quit()
# run_game()
class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (150, 130, 200)
        self.mudkip_speed_factor = 1.5
        self.mudkip_size = (150, 150)


def update_screen(ai_settings, screen, mudkip):
    screen.fill(ai_settings.bg_color)
    mudkip.blitme()
    pygame.display.flip()

def check_events(mudkip):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mudkip)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, mudkip)


def check_keydown_events(event, mudkip):
    if event.key == pygame.K_RIGHT:
            # M Move the ship to the right.
        mudkip.moving_right = True
    elif event.key == pygame.K_LEFT:
        mudkip.moving_left = True
    elif event.key == pygame.K_UP:
        mudkip.moving_up = True
    elif event.key == pygame.K_DOWN:
        mudkip.moving_down = True


def check_keyup_events(event, mudkip):
    if event.key == pygame.K_RIGHT:
        mudkip.moving_right = False
    elif event.key == pygame.K_LEFT:
        mudkip.moving_left = False
    elif event.key == pygame.K_UP:
        mudkip.moving_up = False
    elif event.key == pygame.K_DOWN:
        mudkip.moving_down = False


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Mudkip")
    mudkip = Mudkip(ai_settings, screen)


    while True:
        check_events(mudkip)
        mudkip.update()
        update_screen(ai_settings, screen, mudkip)
    pygame.quit()
run_game()

