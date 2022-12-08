import pygame
from pygame.locals import *
from game_value import *
import pickle
from os import path
from game_image_sound import *

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()  # 마우스 위치

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False


		#draw button
		screen.blit(self.image, self.rect)

		return action


#create buttons
start_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.3), start_img)
option_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2, option_img)
exit_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.15), exit_img)
easy_mode_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), easy_mode_img)
hard_mode_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.1), hard_mode_img)
game_rule_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 + (screen_height*0.1), game_rule_img)
sound_on_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), sound_on_img)
back_img_button = Button(screen_width // 2 - (screen_width*0.47), screen_height // 2 - (screen_height*0.47), back_img)
sound_off_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.1), sound_off_img)
restart_button = Button(screen_width // 2 - (screen_width*0.05), screen_height // 2 + (screen_height*0.1), restart_img)
home_button = Button(screen_width // 2 - (screen_width*0.05), screen_height // 2 - (screen_height*0.1), home_img)
skin_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 - (screen_height*0.15), skin_img)
playing_home_button = Button(screen_width // 2 + (screen_width*0.46) , screen_height // 2 - (screen_height*0.49), playing_home_img)
buy_button1 = Button(screen_width// 2 - (screen_width*0.33), screen_height// 2+(screen_height*0.1), buy_img)
buy_button2 = Button(screen_width// 2 - (screen_width*0.04), screen_height// 2+(screen_height*0.1), buy_img)
buy_button3 = Button(screen_width // 2 + (screen_width*0.26), screen_height// 2+(screen_height*0.1), buy_img)
selected_button = Button(screen_width// 2 - (screen_width*0.36), screen_height// 2+(screen_height*0.1), selected_img)
select_button1 = Button(screen_width// 2 - (screen_width*0.15), screen_height// 2+(screen_height*0.1), select_img)
select_button2 = Button(screen_width // 2 + (screen_width*0.08), screen_height// 2+(screen_height*0.1), select_img)
select_button3 = Button(screen_width // 2 + (screen_width*0.28), screen_height// 2+(screen_height*0.1), select_img)