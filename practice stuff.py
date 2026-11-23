import pygame

class Background():
    def __init__(self, size, ts, player):
        self.size = size      # screen size
        self.ts = ts          # tilesize
        self.player = player  # bring in our shadow warrior
        
        fp = r"AI PNGs\myback.jpg"        # define the file path image
        og_image = pygame.image.load(fp)  # load my image
        self.image = pygame.transform.scale_by(og_image, .45)
        
    def make_bg(self):
        self.bg = pygame.Surface(self.size)      # make a surface
        self.rect = self.bg.get_rect()
        self.bg.blit(self.image, (-100,-10))
        return self.bg
        
    def draw(self, screen):
        # get offset
        offset_x = (screen.get_width() // 2) - self.player.rect.centerx
        offset_y = ((screen.get_height() // 2) - self.player.rect.centery)
        
        # blit the background shifted by that offset
        screen.blit(self.bg, (offset_x - 10, offset_y))
