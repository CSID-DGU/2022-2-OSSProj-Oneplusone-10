import pygame
from pygame.locals import *
from pygame import mixer
import pickle


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()


#load images
background_img = pygame.image.load('img/background.png')
restart_img = pygame.image.load('img/restart_bt.png')
start_img = pygame.image.load('img/start_bt.png')
option_img = pygame.image.load('img/option_bt.png')
score_img = pygame.image.load('img/score_bt.png')
exit_img = pygame.image.load('img/exit_bt.png')
easy_mode_img = pygame.image.load('img/easy_mode_bt.png')
hard_mode_img = pygame.image.load('img/hard_mode_bt.png')
game_rule_img = pygame.image.load('img/game_rule_bt.png')
sound_on_img = pygame.image.load('img/sound_on_bt.png')
sound_off_img = pygame.image.load('img/sound_off_bt.png')
home_img = pygame.image.load('img/home_bt.png')
back_img = pygame.image.load('img/back_bt.png')
game_rule_page = pygame.image.load('img/game_rule_pg.jpg')
skin_img = pygame.image.load('img/skin_bt.png')
playing_home_img = pygame.image.load('img/playing_home_bt.png')
ako_img =pygame.image.load('img/ako1.png')
winter_ako_img = pygame.image.load('img/winter_ako1.png')
school_ako_img = pygame.image.load('img/school_ako1.png')
graduation_ako_img = pygame.image.load('img/graduation_ako1.png')
coin_img = pygame.image.load('img/coin.png')
buy_img = pygame.image.load('img/buy_bt.png')
select_img = pygame.image.load('img/select_bt.png')
selected_img = pygame.image.load('img/selected_bt.png')

#load sounds
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('img/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('img/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('img/game_over.wav')
game_over_fx.set_volume(0.5)