#font, fontcolor
#player lava, enemy

import pygame
from pygame.locals import *
import pickle
from os import path

from game_value import * #role출력에 사용될 screen 너비와 높이 지정을 위한 game_value 모듈 import
from game_image_sound import * #role 요소의 그림 출력을 위한 game_image_sound 모듈 import
from game_setting import * #게임 실행화면 위에 출력해야하기 때문에 game_settine 모듈 import

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


#기본 폰트 지정
font = pygame.font.Font('Puradak Gentle Gothic OTF.otf', 50)
font_score = pygame.font.Font('Puradak Gentle Gothic OTF.otf', 20)

#기본 색상 지정
white = (255, 255, 255)
blue = (0, 0, 255)


#용암 클래스
class Lava(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self) #Sprite는 게임에서 나타내는 모든 캐릭터, 장애물등을 표현할 때 사용하는 Surface임(Sprite를 사용하면 Sprite 그룹을 만들어서 모두 한꺼번에 움직이게 하거나 Sprite들끼리의 충돌등을 알아낼 수 있다)
		img = pygame.image.load('img/lava.png') #용암 이미지 load하기 (게임에서 이미지 사용하기 위해 이미지 불러와서 변수에 저장)
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2)) #이미지 크기 규격화
		self.rect = self.image.get_rect() #이미지 정사각형으로 규격화
		self.rect.x = x
		self.rect.y = y


#슬라임(장애물)클래스
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/blob.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0

	def update(self): #enemy(슬라임)의 이동
		self.rect.x += self.move_direction #가로로만 움직이게 설정
		self.move_counter += 1
		if abs(self.move_counter) > 50: #게임 화면의 맨끝으로 이동할 시 돌아오도록
			self.move_direction *= -1
			self.move_counter *= -1
