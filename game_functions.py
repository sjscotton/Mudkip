import pygame
import sys
from berry import Berry
from berry import AnimatedBerry
from rain_drops import RainDrop
from pygame.locals import *

def update_screen(ai_settings, screen, mudkip, berries, rain, animated_berries):
    screen.fill(ai_settings.bg_color)

    mudkip.blitme()
    for berry in berries.sprites():
        berry.blitme()
    for raindrop in rain:
        raindrop.update()
        raindrop.blitme()
        update_animated_berries(ai_settings, screen, animated_berries)
    pygame.display.flip()

def update_animated_berries(ai_settings, screen, animated_berries):

    for animated_berry in animated_berries.sprites():
        if animated_berry.steps > 160 :
            animated_berries.remove(animated_berry)
        animated_berry.update()
        animated_berry.blitme()


def check_events(ai_settings, screen, rain, mudkip):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == USEREVENT+1:
            add_rain(ai_settings, screen, rain)
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

def check_for_berries(ai_settings, screen, berries, animated_berries):
    if len(berries) == 0 and len(animated_berries) == 0:
        add_berry(ai_settings, screen, berries)

def check_mudkip_berry_collisions(ai_settings, screen, mudkip, berries, animated_berries):
    #collisions = pygame.sprite.spritecollide(mudkip, berries, True)
    """top one also works, but dosent give me freedom to act apon the collision"""
    # if collisions:
    # pygame.sprite.spritecollide(mudkip, berries, True)

    for berry in berries:
        if pygame.sprite.collide_rect(berry, mudkip):
            ai_settings.sound_a.play()

            berry_clone = clone(ai_settings, screen, berry)
            animated_berries.add(berry_clone)

            berries.remove(berry)
def clone(ai_settings, screen, berry):

    berry_clone = AnimatedBerry(ai_settings, screen, berry)
    berry_clone.rect.centerx = berry.rect.centerx
    berry_clone.rect.centery = berry.rect.centery
    berry_clone.initial_y_pos = berry.rect.centery
    berry_clone.blitme()
    return berry_clone


def add_rain(ai_settings, screen, rain):
    ''' adds new rain, and removes old raindrops'''
    raindrop = RainDrop(ai_settings, screen)
    rain.add(raindrop)
    for raindrop in rain.copy():
        if raindrop.rect.top > ai_settings.screen_height :
            rain.remove(raindrop)




