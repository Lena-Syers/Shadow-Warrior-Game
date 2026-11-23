import pygame

def make_bg(size):
    bg = pygame.Surface(size)
    # fill it
    sandy_color = (255, 207, 156)
    bg.fill(sandy_color)
    return bg
