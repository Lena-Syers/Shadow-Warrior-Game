import pygame

class Background():
    def __init__(self, size, ts, player):
        self.size = size      # screen size
        self.ts = ts          # tilesize
        self.player = player  # bring in our shadow warrior
        
        fp_back = r"AI PNGs\myback.jpg"        # define the file paths of the images        
#       fp2 = r"AI PNGs\myback2.jpg"
        og_image_back = pygame.image.load(fp_back)  # load my image
#       og_image2 = pygame.image.load(fp2)
        self.image_back = pygame.transform.scale_by(og_image_back, .45)
#       self.image2 = pygame.transform.scale_by(og_image2, .45)
        self.scroll = 0
        self.v_scroll = 1.5
        self.bg_width = self.image_back.get_width()
        
    def update(self):
        self.scroll -= self.v_scroll       
        if self.scroll <= -self.bg_width:
            self.scroll += self.bg_width
        
    def draw(self, screen):
        # get offset
        offset_y = ((screen.get_height() // 2) - self.player.rect.centery + 90)
        
        # blit the background shifted by that offset
        screen.blit(self.image_back, (self.scroll, offset_y))
        screen.blit(self.image_back, (self.scroll + self.bg_width, offset_y))