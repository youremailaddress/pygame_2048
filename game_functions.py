import os.path
import pygame.event
import pygame.mouse
import pygame.display
import sys
from blocks import Blocks
import random
import time

def initialize_data():
    if os.path.exists('corefile.txt') == False:
        cf = open('corefile.txt', 'w+')
        cf.write(str(0))
        cf.close()

def check_events(sets,screen,sb,play_button,win_and_play_button,
   failed_and_play_button,blocks,music):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(sb,sets,event,blocks,music)
            check_high_score(sb)
            sb.json_high_score()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                if sets.stats == False and sets.win_lose == 0:
                    check_play_button(sets,screen,sb,play_button,
                       blocks,mouse_x,mouse_y)
                elif sets.stats == False and sets.win_lose == 1:
                    check_win_and_play_button(sets,screen,sb,
                       win_and_play_button,blocks,mouse_x,mouse_y)
                elif sets.stats == False and sets.win_lose == -1:
                    check_failed_and_play_button(sets,screen,sb,
                       failed_and_play_button,blocks,mouse_x,mouse_y)
            
def check_play_button(sets,screen,sb,play_button,
        blocks,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not sets.stats:
        pygame.mouse.set_visible(False)
        sb.score = 0
        prep_block(sets,screen,blocks)
        random_set_place(sets,blocks)
        random_set_place(sets,blocks)
        sb.prep_score()
        sb.json_high_score()
        sb.high_score = sb.show_json()
        sb.prep_high_score()
        sets.stats = True

def check_failed_and_play_button(sets,screen,sb,failed_and_play_button,
        blocks,mouse_x,mouse_y):
    button_clicked = failed_and_play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not sets.stats:
        pygame.mouse.set_visible(False)
        sb.score = 0
        prep_block(sets,screen,blocks)
        random_set_place(sets,blocks)
        random_set_place(sets,blocks)
        sb.prep_score()
        sb.json_high_score()
        sb.high_score = sb.show_json()
        sb.prep_high_score()
        sets.stats = True

def check_win_and_play_button(sets,screen,sb,win_and_play_button,
        blocks,mouse_x,mouse_y):
    button_clicked = win_and_play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not sets.stats:
        pygame.mouse.set_visible(False)
        sb.score = 0
        prep_block(sets,screen,blocks)
        random_set_place(sets,blocks)
        random_set_place(sets,blocks)
        sb.prep_score()
        sb.json_high_score()
        sb.high_score = sb.show_json()
        sb.prep_high_score()
        sets.stats = True

                
def check_keydown_events(sb,sets,event,blocks,music):
    if event.key == pygame.K_RIGHT: 
        if sets.stats == True:
            music.shua.play()
            right_tight(blocks,sets)
            m = right_mix(sets,blocks)
            sb.score += m
            right_tight(blocks,sets)
            random_set_place(sets,blocks)
    elif event.key == pygame.K_LEFT:
        if sets.stats == True:
            music.shua.play()
            left_tight(blocks,sets)
            m = left_mix(sets,blocks)
            left_tight(blocks,sets)
            sb.score += m
            random_set_place(sets,blocks)
    elif event.key == pygame.K_UP:  
        if sets.stats == True:
            music.shua.play()
            up_tight(blocks,sets)
            m = up_mix(sets,blocks)
            up_tight(blocks,sets)
            sb.score += m
            random_set_place(sets,blocks)
    elif event.key == pygame.K_DOWN:
        if sets.stats == True:            
            music.shua.play()
            down_tight(blocks,sets)
            m = down_mix(sets,blocks)
            down_tight(blocks,sets)
            sb.score += m
            random_set_place(sets,blocks)
    elif event.key == pygame.K_q:
        sys.exit()

def prep_block(sets,screen,blocks):
    for x in range(sets.lines_and_rows):
        for y in range(sets.lines_and_rows):
            new_block = Blocks (sets,screen)
            new_block.x = x
            new_block.y = y
            blocks.add(new_block)

def update_blocks(blocks):
    blocks.update()
def update_screen(sb,sets,screen,blocks,play_button,win_and_play_button,
       failed_and_play_button):
    screen.fill(sets.bg_color)
    if sets.stats == True:
        for block in blocks.sprites():
            block.draw_blocks()
    sb.prep_score()
    sb.prep_high_score()
    sb.show_score()
    if sets.stats == False and sets.win_lose == 0:
        play_button.draw_button()
    elif sets.stats == False and sets.win_lose == 1:
        win_and_play_button.draw_button()
    elif sets.stats == False and sets.win_lose == -1:
        failed_and_play_button.draw_button()
    pygame.display.flip()
            
def random_set_place(sets,blocks):
    ran1 = random.randint(0,sets.lines_and_rows-1)
    ran2 = random.randint(0,sets.lines_and_rows-1)
    ran3 = random.randint(0,sets.rates_of_2_4)
    if can_place(blocks):
        for block in blocks:
            if (block.x,block.y) == (ran1,ran2) and block.exp == 0:
                if ran3 != 0:
                    block.exp = 1
                else:
                    block.exp = 2
            elif (block.x,block.y) == (ran1,ran2) and block.exp != 0:
                random_set_place(sets,blocks)
def check_mv(sets,blocks):
    if not can_place(blocks):
        if not check_move(sets,blocks):
            sets.win_lose = -1
            sets.stats = False
            blocks.empty()
            time.sleep(2)
            pygame.mouse.set_visible(True)

def check_move(sets,blocks):
    for y in range(0,sets.lines_and_rows):
        for x in range(0,sets.lines_and_rows - 1):
            if resp(x,y,blocks) == resp(x+1,y,blocks):
                return True
    for x in range(0,sets.lines_and_rows):
        for y in range(0,sets.lines_and_rows - 1):
            if resp(x,y,blocks) == resp(x,y+1,blocks):
                return True
    return False

                
def can_place(blocks):
    place_stats = False
    for block in blocks:
        if block.exp == 0:
            place_stats = True
    return place_stats
                         
def left_tight(blocks,sets):
    for y in range(0,sets.lines_and_rows):
        i = get_i_in_left(y,blocks,sets)
        for x in range(0,sets.lines_and_rows):
            if resp(x,y,blocks) != 0 and i < x:
                give_value(resp(x,y,blocks),i,y,blocks)
                give_value(0,x,y,blocks)
                i += 1

def get_i_in_left(y,blocks,sets):
    i = 0
    for x in range(0,sets.lines_and_rows):
        if resp(x,y,blocks) != 0:
            i += 1
        else:
            break
    return i
            
def right_tight(blocks,sets):
    for y in range(0,sets.lines_and_rows):
        j = get_j_in_right(y,blocks,sets)
        for x in range(sets.lines_and_rows - 1,-1,-1):
            if resp(x,y,blocks) != 0 and j > x: 
                give_value(resp(x,y,blocks),j,y,blocks)
                give_value(0,x,y,blocks)
                j -= 1
                  
def get_j_in_right(y,blocks,sets):
    j = 3
    for x in range(sets.lines_and_rows-1,-1,-1):
        if resp(x,y,blocks) != 0:
            j -= 1
        else:
            break
    return j
        
def up_tight(blocks,sets):
    for x in range(0,sets.lines_and_rows):
        k = get_k_in_up(x,blocks,sets)
        for y in range(0,sets.lines_and_rows):
            if resp(x,y,blocks) != 0 and k < y: 
                give_value(resp(x,y,blocks),x,k,blocks)
                give_value(0,x,y,blocks)
                k += 1
                
def get_k_in_up(x,blocks,sets):
    k = 0
    for y in range(0,sets.lines_and_rows):
        if resp(x,y,blocks) != 0:
            k += 1
        else:
            break
    return k
    
def down_tight(blocks,sets):
    for x in range(0,sets.lines_and_rows):
        m = get_m_in_down(x,blocks,sets)
        for y in range(sets.lines_and_rows-1,-1,-1):
            if resp(x,y,blocks) != 0 and m > y: 
                give_value(resp(x,y,blocks),x,m,blocks)
                give_value(0,x,y,blocks)
                m -= 1

def get_m_in_down(x,blocks,sets):
    m = 3
    for y in range(sets.lines_and_rows-1,-1,-1):
        if resp(x,y,blocks) != 0:
            m -= 1
        else:
            break
    return m


        
def resp(x,y,blocks):
    for block in blocks:
        if (block.x , block.y) == (x , y):
            return block.exp

def give_value(value_of_blocks,x,y,blocks):
    for block in blocks:
        if (block.x , block.y) == (x , y):
            block.exp = value_of_blocks

def left_mix(sets,blocks):
    miniscore = 0
    for y in range(0,sets.lines_and_rows):
        for x in range(0,sets.lines_and_rows - 1):
            if resp(x,y,blocks) == resp(x+1,y,blocks) and resp(x,y,blocks)!=0:
                give_value(resp(x,y,blocks) + 1,x,y,blocks)
                give_value(0,x+1,y,blocks)
                miniscore += 2**resp(x,y,blocks)
                if 2**resp(x,y,blocks) == 2048:
                    sets.win_lose = 1
                    sets.stats = False
                    time.sleep(2)
                    blocks.empty()
    return miniscore
    
def right_mix(sets,blocks):
    miniscore = 0
    for y in range(0,sets.lines_and_rows):
        for x in range(sets.lines_and_rows-1,0,-1):
            if resp(x,y,blocks) == resp(x-1,y,blocks) and resp(x,y,blocks)!=0:
                give_value(resp(x,y,blocks) + 1,x,y,blocks)
                give_value(0,x-1,y,blocks)
                miniscore += 2**resp(x,y,blocks)
                if 2**resp(x,y,blocks) == 2048:
                    sets.win_lose = 1
                    sets.stats = False
                    time.sleep(2)
                    blocks.empty()
    return miniscore
    
def up_mix(sets,blocks):
    miniscore = 0
    for x in range(0,sets.lines_and_rows):
        for y in range(0,sets.lines_and_rows - 1):
            if resp(x,y,blocks) == resp(x,y+1,blocks) and resp(x,y,blocks)!=0:
                give_value(resp(x,y,blocks) + 1,x,y,blocks)
                give_value(0,x,y+1,blocks)
                miniscore += 2**resp(x,y,blocks)
                if 2**resp(x,y,blocks) == 2048:
                    sets.win_lose = 1
                    sets.stats = False
                    time.sleep(2)
                    blocks.empty()
    return miniscore
    
def down_mix(sets,blocks):
    miniscore = 0
    for x in range(0,sets.lines_and_rows):
        for y in range(sets.lines_and_rows-1,0,-1):
            if resp(x,y,blocks) == resp(x,y-1,blocks) and resp(x,y,blocks)!=0:
                give_value(resp(x,y,blocks) + 1,x,y,blocks)
                give_value(0,x,y-1,blocks)
                miniscore += 2**resp(x,y,blocks)
                if 2**resp(x,y,blocks) == 2048:
                    sets.win_lose = 1
                    sets.stats = False
                    time.sleep(2)
                    blocks.empty()
    return miniscore

def check_high_score(sb):
    if sb.score >sb.high_score:
        sb.high_score = sb.score
        sb.prep_high_score()    


    
