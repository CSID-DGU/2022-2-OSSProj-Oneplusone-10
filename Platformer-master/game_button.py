#각종 버튼들

import pygame
from pygame.locals import *
import pickle
from os import path

from game_value import *
from game_image_sound import * #버튼 클릭 시 효과음을 위해 game_image_sound 모듈 import

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

#버튼 클래스
class Button():
	def __init__(self, x, y, image):
		self.image = image #이미지 초기화
		self.rect = self.image.get_rect() #규격화 초기화
		self.rect.x = x
		self.rect.y = y
		self.clicked = False #마우스 클릭 안하는 것으로 초기 지정

	def draw(self): 
		action = False

		#마우스 위치 지정
		pos = pygame.mouse.get_pos()  

		#마우스 위치 확인후 클릭할 때 조건마다 해야하는 액션
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		#맨 처음은 클릭 되지 않은 상태로 
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#버튼 출력
		screen.blit(self.image, self.rect)

		return action


#버튼 변환및 위치 지정(이때 위치는 시작 지점의 좌표)
start_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.3), start_img) #main 화면 버튼
option_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2, option_img)
skin_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.15), skin_img)
exit_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.15), exit_img)
easy_mode_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), easy_mode_img) #start 화면 버튼
hard_mode_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.1), hard_mode_img)
game_rule_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.1), game_rule_img) #option 화면 버튼
sound_on_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), sound_on_img)
sound_off_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), sound_off_img)
back_img_button = Button(screen_width // 2 - (screen_width*0.47), screen_height // 2 - (screen_height*0.47), back_img)
restart_button = Button(screen_width // 2 - (screen_width*0.05), screen_height // 2 + (screen_height*0.1), restart_img) #게임 끝나고 보이는 버튼
home_button = Button(screen_width // 2 - (screen_width*0.05), screen_height // 2 - (screen_height*0.1), home_img)
playing_home_button = Button(screen_width // 2 + (screen_width*0.46) , screen_height // 2 - (screen_height*0.49), playing_home_img) #게임 도중 홈으로갈 수 있는 버튼
selected_button = Button(screen_width// 2 - (screen_width*0.36), screen_height// 2+(screen_height*0.1), selected_img) #스킨 페이지 버튼
select_button1 = Button(screen_width// 2 - (screen_width*0.15), screen_height// 2+(screen_height*0.1), select_img)
select_button2 = Button(screen_width // 2 + (screen_width*0.08), screen_height// 2+(screen_height*0.1), select_img)
select_button3 = Button(screen_width // 2 + (screen_width*0.28), screen_height// 2+(screen_height*0.1), select_img)

