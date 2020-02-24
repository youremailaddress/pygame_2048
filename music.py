import pygame.mixer
import sys


class Music():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('./music/bgm.ogg')
        self.shua= pygame.mixer.Sound('./music/flow.wav')
        self.shua.set_volume(0.1)
        self.play_bgm()
        
    def play_bgm(self):
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1,0.4)
        
