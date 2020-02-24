import pygame.font

class Scoreboard():
    def __init__(self,sets,screen,blocks):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.sets = sets
        self.text_color = self.sets.num_color
        self.font = pygame.font.SysFont('notosans',20)
        self.score = 0
        self.prep_score()
        self.high_score = self.show_json()
        self.prep_high_score()
        self.json_high_score()
        
    def prep_score(self):
        rounded_score = int(round(self.score, 0))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,
            self.sets.bg_color)
            
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10
        
    def prep_high_score(self):
        self.high_score = int(round(self.high_score, 0))
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str,True,
                self.text_color,self.sets.bg_color)
            
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def json_high_score(self):
        with open('./corefile.txt', 'w+') as cf:
            cf.write(str(self.high_score))
            cf.close()

    def show_json(self):
        with open('./corefile.txt') as cf:
            return int(cf.read())
            
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)

