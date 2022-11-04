import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height)) #게임윈도우생성
pygame.display.set_caption('Platformer') #캡션생성

#define game variables
tile_size = 50


#load images
sun_img = pygame.image.load('img/sun.png') #background image 로드
bg_img = pygame.image.load('img/sky.png') #background image 로드

def draw_grid(): #타일을 올리기 위한 그리드 설정(별도 설명 x)->5:5로 했다고 하심
	for line in range(0, 20):
		pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
		pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))



class World(): #타일별로 채울 옵션(grass, dirt, nothing)
	def __init__(self, data): 
		self.tile_list = [] 

		#load images
		dirt_img = pygame.image.load('img/dirt.png')
		grass_img = pygame.image.load('img/grass.png')

		row_count = 0
		for row in data: #for loop을 통해 타일 위치 이동
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size)) #1:dirt image(200,200에 맞게 resize)
					img_rect = img.get_rect() #rectangle에 맞게 정제
					img_rect.x = col_count * tile_size #x좌표
					img_rect.y = row_count * tile_size #x좌표
					tile = (img, img_rect) #tile 위치에 맞게 튜플로 저장(), 터미널창에 각각 image와 rec이 나오는 걸 알 수 ㅣㅇㅆ다. 
					self.tile_list.append(tile) #타일 추가
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size)) #2:dirt image
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				col_count += 1 #타일 이동
			row_count += 1

	def draw(self): #타일 반복
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1]) #blit 함수(화면에 올리기)를 이용. tile자체 tile[0], rectangle모형으로 tile[1]



world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0,200,400,600,800,,,
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
[1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
] #찐 게임 화면. 20x20기준. background 설정을 위해 0:nothing/ 1: dirt/ 2:grass




world = World(world_data)

run = True #기본 셋팅
while run:  #실행되는 동안

	screen.blit(bg_img, (0, 0)) #로드한 background img 화면에 올리기
	screen.blit(sun_img, (100, 100)) #로드한 sun img 화면에 올리기
    #sun은 반드시 background 위에 올려야 한다.(background-> sun)

	world.draw()

	draw_grid()

	for event in pygame.event.get(): #(event handler)
		if event.type == pygame.QUIT: #x버튼 누르면 게임 실행 종료
			run = False

	pygame.display.update() #update()를 통해 화면 올릴 수 있다.

pygame.quit()