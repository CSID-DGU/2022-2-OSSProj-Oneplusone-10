#출력할 글씨와 각종 그림과 효과음 및 bgm

import pygame
from pygame.locals import *
import pickle

from game_value import * #글씨에 적용될 screen 너비와 높이 지정을 위한 game_value 모듈 import
from pygame import mixer #소리 사용을 위해 pygame에 내장되어있는 mixer모듈 import


screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE) 


#소리 재생할 수 있는 mixer 초기화
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()


#글씨 출력 함수
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)  
	screen.blit(img, (x, y))  # screen.blit(이미지, 대상) -> 이미지 복사


# 이미지 load하기
# 게임에서 이미지 사용하기 위해 이미지 불러와서 변수에 저장
# 여기저기서 사용해야하므로 전역변수에 저장
background_img = pygame.image.load('img/background.png') #배경화면 이미지
start_img = pygame.image.load('img/start_bt.png')#메인화면 버튼 이미지
skin_img = pygame.image.load('img/skin_bt.png')
option_img = pygame.image.load('img/option_bt.png')
exit_img = pygame.image.load('img/exit_bt.png')
easy_mode_img = pygame.image.load('img/easy_mode_bt.png') #start화면 버튼 이미지
hard_mode_img = pygame.image.load('img/hard_mode_bt.png')
restart_img = pygame.image.load('img/restart_bt.png') #게임 끝날 때 보일 버튼 이미지
playing_home_img = pygame.image.load('img/playing_home_bt.png')
sound_on_img = pygame.image.load('img/sound_on_bt.png') #option화면 버튼 이미지
sound_off_img = pygame.image.load('img/sound_off_bt.png')
game_rule_img = pygame.image.load('img/game_rule_bt.png') 
game_rule_page = pygame.image.load('img/game_rule_pg.jpg')
home_img = pygame.image.load('img/home_bt.png') #모든 화면에 보일 버튼 이미지
back_img = pygame.image.load('img/back_bt.png')
ako_img =pygame.image.load('img/ako1.png') #캐릭터 이미지
winter_ako_img = pygame.image.load('img/winter_ako1.png')
school_ako_img = pygame.image.load('img/school_ako1.png')
graduation_ako_img = pygame.image.load('img/graduation_ako1.png')
coin_img = pygame.image.load('img/coin.png') #코인 이미지
select_img = pygame.image.load('img/select_bt.png') #스킨 선택 이미지
selected_img = pygame.image.load('img/selected_bt.png')

#이제 안쓰는 버튼
#buy_img = pygame.image.load('img/buy_bt.png')
#score_img = pygame.image.load('img/score_bt.png')


#소리 load하기
pygame.mixer.music.load('img/music.wav')
pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('img/coin.wav') #코인 획득할 때 출력되는 소리
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('img/jump.wav') #점프할 때 출력되는 소리
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('img/game_over.wav') #캐릭터가 죽을 때(lava 및 enemy와 접촉 시) 출력되는 소리
game_over_fx.set_volume(0.5)