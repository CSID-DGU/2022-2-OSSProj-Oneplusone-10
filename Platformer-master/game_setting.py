#게임 셋팅에 필요한 요소 _ Platform, Window, Exit, Coin

import pygame
from pygame.locals import *
from game_value import *
import pickle
from os import path

from game_image_sound import * #게임 실행시 필요한 그림을 위해 game_image_sound 모듈 import
from game_rule import * #게임 실행 시 캐릭터들 출력을 위해 game_role 모듈 import

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)


# 각 스프라이트 마다 group을 지정
blob_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

#게임 실행 클래스
class World():
	def __init__(self, data):
		self.tile_list = []

		#이미지 load하기
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')

		row_count = 0
		for row in data:
			col_count = 0
			#클릭 횟수에 따라 타일의 이미지 및 모드 변환
			for tile in row:
				if tile == 1: #한 번 클릭하면 진흙(dirt)로 변경
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))#이미지 크기 규격화
					img_rect = img.get_rect() #이미지 정사각형으로 규격화
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2: #두 번 클릭하면 잔디(grass)로 변경
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect() 
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3: #세 번 클릭하면 슬라임(blob)로 변경
					blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
					blob_group.add(blob) #게임 화면에 나타낼 blob 그룹에 추가
				if tile == 4: #네 번 클릭하면 가로로 이동하는 바(platform)로 변경
					platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
					platform_group.add(platform)
				if tile == 5: #다섯 번 클릭하면 세로로 이동하는 바(platform)로 변경
					platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
					platform_group.add(platform)
				if tile == 6: #여섯 번 클릭하면 용암(lava)로 변경
					lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
					lava_group.add(lava)
				if tile == 7: #일곱 번 클릭하면 코인(coin)로 변경
					coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
					coin_group.add(coin)
				if tile == 8: #여덟 번 클릭하면 탈출구(exit)로 변경
					exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
					exit_group.add(exit)
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1]) #screen 객체 안에 이미지 복사해서 넣기


#이동 바 클래스
class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, move_x, move_y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/platform.png') #이미지 로드
		self.image = pygame.transform.scale(img, (tile_size, tile_size // 2)) #이미지 크기 규격화
		self.rect = self.image.get_rect() #이미지 정사각형으로 규격화
		self.rect.x = x
		self.rect.y = y
		self.move_counter = 0
		self.move_direction = 1
		self.move_x = move_x #가로로 이동할 수 있는 변수 초기화
		self.move_y = move_y #세로로 이동할 수 있는 변수 초기화

	def update(self): #이동 바 움직이는 함수
		self.rect.x += self.move_direction * self.move_x #가로 경로
		self.rect.y += self.move_direction * self.move_y #세로 경로
		self.move_counter += 1 #한칸 씩 움직이도록
		if abs(self.move_counter) > 50: #게임 화면의 끝까지 갈 경우, 다시 돌아오도록
			self.move_direction *= -1
			self.move_counter *= -1  


#탈출 클래스
class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/exit.png')
		self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y


#코인 클래스
class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('img/homework.png')
		self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
