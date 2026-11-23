import pygame
from scene import Background
from shadow_warrior import Shadow
from baddies import Spike
from random import randint

TS = 64
SIZE = (TS*12, TS*8)

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)

# make shadow warrior
shadow = Shadow(190, 362)

# get bg
bg = Background(SIZE, TS, shadow)    # call Background class

# make some spikes
spikes = pygame.sprite.Group()

for i in range(20):
    spikes.add(Spike(randint(1, SIZE[0]), randint(1, SIZE[1])))

running = 1
while running:
    clock.tick(60)
    # update everything
    shadow.update()
    shadow.update_image()            # keep him moving
    bg.update()
    
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        shadow.check_keys(e)
    
    # draw the background and the warrior on top
    bg.draw(screen)
    shadow.draw(screen)              # draw our shadow warrior
    #spikes.draw(screen)

    # Flip the screen
    pygame.display.flip()

pygame.quit()