import pygame

class Shadow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # player position
        self.x = x
        self.y = y
        self.ground_y = y
        # file paths
        self.fp_front = r"AI PNGs\lvl1_front.png"
        self.fp_s1 = r"AI PNGs\lvl1_s1.png"
        self.fp_s2 = r"AI PNGs\lvl1_s2.png"
        self.fp_s3 = r"AI PNGs\lvl1_s3.png"
        self.fp_j_s1 = r"AI PNGs\jumps\lvl1_jump_s1.png"
        self.fp_j_s2 = r"AI PNGs\jumps\lvl1_jump_s2.png"
        self.fp_j_s3 = r"AI PNGs\jumps\lvl1_jump_s3.png"
        # load the images
        self.og_front = pygame.image.load(self.fp_front)
        self.og_s1 = pygame.image.load(self.fp_s1)
        self.og_s2 = pygame.image.load(self.fp_s2)
        self.og_s3 = pygame.image.load(self.fp_s3)
        self.og_j_s1 = pygame.image.load(self.fp_j_s1)
        self.og_j_s2 = pygame.image.load(self.fp_j_s2)
        self.og_j_s3 = pygame.image.load(self.fp_j_s3)
        # scale the images
        self.front = pygame.transform.scale_by(self.og_front, .14)
        self.step1 = pygame.transform.scale_by(self.og_s1, .14)
        self.step2 = pygame.transform.scale_by(self.og_s2, .14)
        self.step3 = pygame.transform.scale_by(self.og_s3, .14)
        self.rect = self.front.get_rect(center=(self.x, self.y)) # rect
        self.j_s1 = pygame.transform.scale_by(self.og_j_s1, .14)
        self.j_s2 = pygame.transform.scale_by(self.og_j_s2, .14)
        self.j_s3 = pygame.transform.scale_by(self.og_j_s3, .14)
        self.images = [self.step1, self.step2, self.step3] # walking frames list
        self.j_images = [self.j_s1, self.j_s2, self.j_s3]  # jumping frames list
        self.image_idx = 0
        self.j_image_idx = 0
        # walking parameters
        self.walk_delta = 200 # ms
        self.walk_time = 0
        #jumping parameters
        self.jump_delta = 150
        self.jump_time = 0
        self.is_jumping = False # this will be our made up jump function
        self.vx = 0
        self.vy = 0
        self.ds = .1
        self.gravity = .3
        
        
    def update(self):
        if self.is_jumping:
            self.vy += self.gravity
            self.y += self.vy
            
            t_now = pygame.time.get_ticks() 
            if t_now - self.jump_time > self.jump_delta:    
                self.jump_time = t_now
                self.image = self.j_images[self.j_image_idx]
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.j_image_idx +=1
                self.j_image_idx = self.j_image_idx % len(self.j_images)
                if self.j_image_idx > len(self.j_images):
                    self.j_image_idx = len(self.j_images) - 1
             
            if self.y >= self.ground_y:
                self.y = self.ground_y
                self.vy = 0
                self.j_image_idx = 0
                self.is_jumping = False
                
                self.image_idx = 0
                self.image = self.images[self.image_idx]
                self.walk_time = pygame.time.get_ticks()
        
        else:
            self.x += self.vx
        
        self.rect.center = (self.x, self.y)
        print(f"Shadow Warrior: {self.x}, {self.y}")
         
    def update_image(self):
        if not self.is_jumping:
            t_now = pygame.time.get_ticks()
            if t_now - self.walk_time > self.walk_delta:
                self.walk_time = t_now
                self.image_idx +=1
                self.image_idx = self.image_idx % len(self.images)
                self.image = self.images[self.image_idx]
    
    
    def check_keys(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT:
                print("RIGHT ARROW")
                self.vx += self.ds
            if e.key == pygame.K_LEFT:
                print("LEFT ARROW")
                self.vx = 0
            if e.key == pygame.K_UP:
                if not self.is_jumping:
                    print("JUMP!")
                    self.is_jumping = True
                    self.vy = -5
                    self.jump_time = pygame.time.get_ticks()
                    self.j_image_idx = 0
                    if self.j_images:
                        self.image = self.j_images[0]
    
    def draw(self, screen):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, (self.rect))
        