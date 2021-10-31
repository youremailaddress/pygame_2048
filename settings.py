import pygame.font

class Settings():
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 400
        self.bg_color = (250,248,239)
        self.lines_and_rows = 4
        self.font = pygame.font.SysFont('notosans',20)
        self.blocks_color = (205,193,180)
        self.num_color = (119,110,101)
        self.rates_of_2_4 = 9
        self.stats = False
        self.win_lose = 0
