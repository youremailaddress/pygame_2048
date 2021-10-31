# coding: utf-8
import pygame.display
from settings import Settings
import game_functions as gf
from music import Music
from blocks import Blocks
import time
from pygame.sprite import Group
from scoreboard import Scoreboard
from button import Button


def run_game():
    pygame.init()
    gf.initialize_data() 
    sets = Settings()
    music = Music()
    screen = pygame.display.set_mode(
        (sets.screen_width,sets.screen_height))
    pygame.display.set_caption("2048")
    play_button = Button(sets,screen,"Play!")
    failed_and_play_button = Button(sets,screen,"Try again")
    win_and_play_button = Button(sets,screen,"Win! New Game!")
    blocks = Group()
    sb = Scoreboard(sets,screen,blocks)
    while True:
        gf.check_events(sets,screen,sb,play_button,win_and_play_button,
           failed_and_play_button,blocks,music)
        
        if sets.stats:
            gf.update_blocks(blocks)
        gf.update_screen(sb,sets,screen,blocks,play_button,win_and_play_button,
              failed_and_play_button)
        gf.check_mv(sets,blocks)
run_game()
