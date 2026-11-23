import pygame

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        fp_spike = r"AI PNGs\spike_ball.png"
        og_image_spike = pygame.image.load(fp_spike)  # load my image
        self.image = pygame.transform.scale_by(og_image_spike, .003)
        
        # spike position
        self.x = x
        self.y = y
        
        self.rect = self.image.get_rect(center=(self.x, self.y))

