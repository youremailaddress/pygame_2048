import pygame.font
import pygame.rect
from pygame.sprite import Sprite

class Blocks(Sprite):
    def __init__(self,sets,screen):
        super(Blocks,self).__init__()
        self.screen = screen
        self.sets = sets
        self.width,self.height = 80 , 80
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.blocks_color = sets.blocks_color
        self.lines_and_rows = sets.lines_and_rows 
        self.num_color = sets.num_color
        self.font = sets.font
        self.x = 0
        self.y = 0
        self.exp = 0
        self.msg_image = None
        
    def update(self):
        self.rect.left =40 + (self.x)*(self.width)
        self.rect.top =40 + (self.y)*(self.height)
        self.blocks_color = (205-10*(self.exp),193+5*(self.exp),180)
        self.prep_msg()
            
    def draw_blocks(self):
            self.screen.fill(self.blocks_color,self.rect)
            if self.exp != 0 and self.msg_image:
                self.screen.blit(self.msg_image,self.msg_image_rect)
            elif self.exp != 0 and self.msg_image == None:
                pass
    def prep_msg(self):
        if self.exp != 0:
            self.msg_image = self.font.render(str(2**self.exp),True,
              self.num_color,self.blocks_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
        
