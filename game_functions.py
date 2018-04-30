import pygame
import sys
from berry import Berry

def update_screen(ai_settings, screen, mudkip, berries):
    screen.fill(ai_settings.bg_color)
    # for mudkip in mudkip.sprites():
    mudkip.blitme()
    for berry in berries.sprites():
        berry.blitme()
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
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, mudkip):
    if event.key == pygame.K_RIGHT:
        mudkip.moving_right = False
    elif event.key == pygame.K_LEFT:
        mudkip.moving_left = False
    elif event.key == pygame.K_UP:
        mudkip.moving_up = False
    elif event.key == pygame.K_DOWN:
        mudkip.moving_down = False

def add_berry(ai_settings, screen, berries):
    berry = Berry(ai_settings, screen)
    berries.add(berry)

def check_for_berries(ai_settings, screen, berries):
    if len(berries) == 0:
        add_berry(ai_settings, screen, berries)

def check_mudkip_berry_collisions(ai_settings, screen, mudkip, berries):
    #collisions = pygame.sprite.spritecollide(mudkip, berries, True)
    """top one also works, but dosent give me freedom to act apon the collision"""
    # if collisions:
    # pygame.sprite.spritecollide(mudkip, berries, True)

    for berry in berries:
        if pygame.sprite.collide_rect(berry, mudkip):
            ai_settings.sound_a.play()
            berries.remove(berry)

            # if berry in collisions.values():
            #     print('berry')



