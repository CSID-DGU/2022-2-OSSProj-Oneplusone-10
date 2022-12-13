import pygame
from pygame.locals import *
from pygame import mixer
from game_value import *
import pickle
from os import path

from game_button import *
from game_setting import *
from game_rule import *

clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('Platformer')



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)  
    screen.blit(img, (x, y))  # screen.blit(이미지, 대상) -> 이미지 복사


#function to reset level
def reset_level(level):
    player.reset(100, start_height)
    blob_group.empty()
    platform_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()

    #load in level data and create world
    if path.exists(f'level_data/level{level}_data'):  # 파일 또는 폴더 존재 여부 확인
        pickle_in = open(f'level_data/level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)
    #create dummy coin for showing the score
    score_coin = Coin(coin_tile_size, coin_tile_size)
    coin_group.add(score_coin)
    return world 

def reset_hard_level(hard_level):
    player.reset(100, start_height)
    blob_group.empty()
    platform_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()

    #load in level data and create world
    if path.exists(f'level_data/hard_level{hard_level}_data'):  # 파일 또는 폴더 존재 여부 확인
        pickle_in = open(f'level_data/hard_level{hard_level}_data', 'rb')
        hard_world_data = pickle.load(pickle_in)
    hard_world = World(hard_world_data)
    #create dummy coin for showing the score
    score_coin = Coin(coin_tile_size, coin_tile_size)
    coin_group.add(score_coin)
    return hard_world 


class Player():
    ako = "ako"
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_fx.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1 
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0	
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            self.in_air = True
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
                game_over_fx.play()

            #check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                game_over_fx.play()

            #check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # x방향과 y방향 모두 충돌이 발생하도록 설정
            #check for collision with platforms
            for platform in platform_group:
                #collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1  # 캐릭터를 한 픽셀 위에 넣기 위해
                        self.in_air = False
                        dy = 0
                    #move sideways with the platform  -> 캐릭터가 플랫폼과 함께 직접 좌우이동
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction


            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        
        elif game_over == -1:   
            self.image = self.dead_image
            draw_text('GAME OVER!', font, blue, (screen_width // 2) - (screen_width*0.2), screen_height // 2)
            if self.rect.y > 200:   # 죽으면 유령으로 바뀌고 설정한 범위만큼 위로 올라감
                self.rect.y -= 5   
            
            
        #draw player onto screen
        screen.blit(self.image, self.rect)

        return game_over


    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/{self.ako}{num}.png')
            img_right = pygame.transform.scale(img_right, inplay_ako_size)
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True

player = Player(100, start_height)

#create dummy coin for showing the score
score_coin = Coin(coin_tile_size, coin_tile_size)
coin_group.add(score_coin)

# 맵 로드해주는 코드를 이지모드와 하드모드로 구분하여 진행하므로 각각의 게임 모드안에 reset_level 함수를 호출하여 맵을 로드시킴 
# load in level data and create world 
# if path.exists(f'level{level}_data'):
# 	pickle_in = open(f'level{level}_data', 'rb')
# 	world_data = pickle.load(pickle_in)
# world_easy = World(world_data)

# if path.exists(f'hard_level{hard_level}_data'):
# 	pickle_in = open(f'hard_level{hard_level}_data', 'rb')
# 	hard_world_data = pickle.load(pickle_in)
# world_hard = World(hard_world_data)



run = True
while run:
    # print(main_menu)
    clock.tick(fps)


    screen.blit(background_full_img, (0, 0))
    screen.blit(background_img, (0, 0))
        
    if main_menu == True:
        screen.blit(background_main_img, (0, 0))
        if exit_button.draw(): # exit 버튼 누르면 while 반복 루프에서 벗어남
            run = False     
        if start_button.draw(): # start 버튼 누르면 
            main_menu = "main_screen" #2
        if skin_button.draw(): # store 버튼 누르면 
            main_menu = "skin" #3
        if option_button.draw(): # option 버튼 누르면 
            main_menu = "option" #4
   
    
    elif main_menu == "main_screen":  #2 start 버튼 눌렀을때 페이지 
        screen.blit(background_img, background_coordinate)

        if back_img_button.draw():  # 뒤로가기 버튼 기능 구현 -> 메인 메뉴 페이지로
            main_menu = True
        if easy_mode_button.draw(): # easy mode 버튼 눌렀을때 게임 실행
            main_menu = "easy"
            start_ticks = pygame.time.get_ticks() #시작 시간 설정
            total_time = easy_timer #초안 그래도 10분, 600초로 설정(임시)
            flag = False
            tag = False
        if hard_mode_button.draw(): 
            main_menu = "hard"
            start_ticks = pygame.time.get_ticks() #시작 시간 설정
            total_time = hard_timer #초안 그래도 10분, 600초로 설정(임시)
            flag = False
   
    elif main_menu == "skin":  #3 skin 버튼 눌렀을때 페이지 
        screen.blit(background_img, background_coordinate)

        if back_img_button.draw():  # 뒤로가기 버튼 기능 구현 -> 메인 메뉴 페이지로
            main_menu = True 

        black = (0,0,0) #검정

        #기본 아코
        ako_img = pygame.transform.scale(ako_img, skin_ako_size)
        screen.blit(ako_img, (screen_width // 2 - (screen_width*0.42),screen_height // 2 - (screen_height*0.15)))
        if select_button1.draw():
            player.ako = "ako" # 겨울아코로 변경

        #겨울 아코
        winter_ako_img = pygame.transform.scale(winter_ako_img, skin_winter_ako_size)
        screen.blit(winter_ako_img, (screen_width // 2 - (screen_width*0.23),screen_height // 2 - (screen_height*0.165)))
        if select_button2.draw():
            player.ako = "winter_ako" # 겨울아코로 변경
            
        #과잠 아코
        school_ako_img = pygame.transform.scale(school_ako_img, skin_school_ako_size)
        screen.blit(school_ako_img, ((screen_width // 2 + (screen_width*0.01), screen_height // 2 - (screen_height*0.15))))
        if select_button3.draw():
            player.ako = "school_ako" # 스쿨아코로 변경

        #졸업 아코
        graduation_ako_img = pygame.transform.scale(graduation_ako_img, skin_graduation_ako_size)
        screen.blit(graduation_ako_img, (screen_width // 2 + (screen_width*0.22),screen_height // 2 - (screen_height*0.15)))
        if select_button4.draw():
            player.ako = "graduation_ako" # 졸업아코로 변경
  

    elif main_menu == "option":  # 4 option 버튼 눌렀을때 페이지(디폴트 : 소리켜져있음)
        screen.blit(background_img, background_coordinate)
        pygame.mixer.music.unpause() 
        if back_img_button.draw():
            main_menu = True
        if sound_off_button.draw(): #sound on 버튼 누르면 음악 임시멈춤
            main_menu="option_soundoff" #4.3
        if game_rule_button.draw() :
            main_menu = "game_rule" #4.7

    elif main_menu == "option_soundoff": #4.3 옵션화면_소리 껐을때
        pygame.mixer.music.pause()
        if back_img_button.draw():
            main_menu = True
        if sound_on_button.draw(): #sound off 버튼 누르면 음악 다시 시작
            main_menu= "option" #4
        if game_rule_button.draw() :
            main_menu = "game_rule" #4.7
        

    elif main_menu == "game_rule": #게임 룰 페이지 4.7
        screen.blit(background_img, background_coordinate)
        screen.blit(game_rule_page, background_coordinate)
        if back_img_button.draw():  # 뒤로가기 버튼 기능 구현 -> 옵션 페이지로
            if pygame.mixer.music. get_busy ( ) :
                main_menu = "option" #4
            elif not pygame.mixer.music. get_busy ( ) :
                main_menu = 4.3
    
    elif main_menu == 'easy' and not flag:
        flag = True
        world = reset_level(level)
        world.draw()


    elif main_menu == "easy" and flag:
        world.draw()
        
        if playing_home_button.draw():
            main_menu = True
            level = 1
   
        if game_over == 0:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 타이머 시간을 1000으로 나누어 초단위로 표시 (default: ms 단위)
            game_font = pygame.font.Font('Puradak Gentle Gothic OTF.otf', game_font_size)

            timer = game_font.render(str(int(easy_timer - elapsed_time)), True, timer_text_color) # 색상 시정
            screen.blit(timer, timer_coordinate) # 타이머 위치 지정
            if easy_timer - elapsed_time <= game_over_time: 
                restart_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 , restart_img)
                if restart_button.draw():
                    main_menu = "main_screen"
                if exit_button.draw():
                    main_menu = True

            blob_group.update()
            platform_group.update()
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()  # 코인 먹을때 사운드 실행
            draw_text('X ' + str(score), font_score, white, coin_score_text_x, coin_score_text_y)  # 코인 스코어 왼쪽 상단에 가시화
        
        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        #if player has died
        if game_over == -1:
                world_data = []
                world = reset_level(level)
                game_over = 0
                # score = 0   # 획득한 코인 리셋 안되게 이코드 주석
                
        #if player has completed the level
        if game_over == 1:
            #reset game and go to next level
            level += 1
            if level <= max_levels:
                #reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
                
            elif score <= 5:
                draw_text('과제물 획득 수가 부족합니다', font, blue, screen_width // 2 - (screen_width*0.3), screen_height // 2)
                draw_text('기록 갱신 불가 !', font, white, screen_width // 2 - (screen_width*0.15), screen_height // 2+ (screen_height*0.05))
                final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                screen.blit(final_timer, (350,10)) # 타이머 위치 지정
                
                if home_button.draw():
                    main_menu = True
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
     
                elif restart_button.draw():
                    main_menu = 'easy'
                    start_ticks = pygame.time.get_ticks() #시작 시간 설정
                    total_time = easy_timer # easy_mode 타이머 100초
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                
                
                
            else:
                if elapsed_time <= easy_record:
                    easy_record = elapsed_time
                    draw_text('축하합니다 ! :)', font, blue, screen_width // 2 - (screen_width*0.15), screen_height // 2)
                    draw_text('현재 최고 기록 : ' + str(easy_record), font, white, screen_width // 2 - (screen_width*0.22), screen_height // 2+ (screen_height*0.05))
                    #draw_text('an established record : nn, the current record : mm', font, white, (screen_width // 2), screen_height // 2)
                    final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                    screen.blit(final_timer, (350,10)) # 타이머 위치 지정
                    
                    
                else:
                    draw_text('최고 기록 갱신 실패', font, blue, screen_width // 2 - (screen_width*0.15), screen_height // 2)
                    draw_text('현재 최고 기록 : ' + str(easy_record), font, white, screen_width // 2 - (screen_width*0.22), screen_height // 2+ (screen_height*0.05))
                    final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                    screen.blit(final_timer, (350,10)) # 타이머 위치 지정
                    
                    
                if home_button.draw():
                    main_menu = True
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
     
                elif restart_button.draw():
                    main_menu = 'easy'
                    start_ticks = pygame.time.get_ticks() #시작 시간 설정
                    total_time = easy_timer 
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
        
                    
    elif main_menu == 'hard' and not flag:
        flag = True
        world = reset_hard_level(level)
        world.draw()
  
    elif main_menu == "hard" and flag:
        world.draw()
        if playing_home_button.draw():
            main_menu = True
            hard_level = 1
   
        if game_over == 0:
            elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 타이머 시간을 1000으로 나누어 초단위로 표시 (default: ms 단위)
            game_font = pygame.font.Font('Puradak Gentle Gothic OTF.otf', game_font_size)
            timer = game_font.render(str(int(hard_timer - elapsed_time)), True, timer_text_color) # 타이머 위치 지정
            screen.blit(timer, timer_coordinate) # 타이머 위치 지정
            
            if hard_timer - elapsed_time <= game_over_time: 
                restart_button = Button(screen_width // 2 - (screen_width*0.16), screen_height // 2 , restart_img)
                if restart_button.draw():
                    main_menu = "main_screen"
                if exit_button.draw():
                    main_menu = True
            blob_group.update()
            platform_group.update()
            #update score
            #check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_fx.play()
            draw_text('X ' + str(score), font_score, white, coin_score_text_x, coin_score_text_y)
        
        blob_group.draw(screen)
        platform_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        #if player has died
        if game_over == -1:
                hard_world_data = []
                world = reset_hard_level(hard_level)
                game_over = 0
                # score = 0   # 획득한 코인 리셋 안되게 이코드 주석

        #if player has completed the level
        if game_over == 1:
            #reset game and go to next level
            hard_level += 1
            if hard_level <= hard_max_levels:
                #reset hard_level
                hard_world_data = []
                world = reset_hard_level(hard_level)
                game_over = 0
                
            elif score <= 45:
                draw_text('과제물 획득 수가 부족합니다', font, blue, screen_width // 2 - (screen_width*0.3), screen_height // 2)
                draw_text('기록 갱신 불가 !', font, white, screen_width // 2 - (screen_width*0.15), screen_height // 2+ (screen_height*0.05))
                final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                screen.blit(final_timer, (350,10)) # 타이머 위치 지정
                
                if home_button.draw():
                    main_menu = True
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
     
                elif restart_button.draw():
                    main_menu = 'hard'
                    start_ticks = pygame.time.get_ticks() #시작 시간 설정
                    total_time = easy_timer # easy_mode 타이머 100초
                    level = 1
                    #reset level
                    world_data = []
                    world = reset_hard_level(level)
                    game_over = 0
                    
            else:
                if elapsed_time <= hard_record:
                    hard_record = elapsed_time
                    draw_text('축하합니다 ! :)', font, blue, screen_width // 2 - (screen_width*0.15), screen_height // 2)
                    draw_text('현재 최고 기록 : ' + str(hard_record), font, white, screen_width // 2 - (screen_width*0.2), screen_height // 2+ (screen_height*0.05))
                    #draw_text('an established record : nn, the current record : mm', font, white, (screen_width // 2), screen_height // 2)
                    final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                    screen.blit(final_timer, (screen_width*0.35, screen_height*0.01)) # 타이머 위치 지정
                    
                else:
                    draw_text('최고 기록 갱신 실패', font, blue, screen_width // 2 - (screen_width*0.15), screen_height // 2)
                    draw_text('현재 최고 기록 : ' + str(hard_record), font, white, screen_width // 2 - (screen_width*0.2), screen_height // 2+ (screen_height*0.05))
                    final_timer = game_font.render('게임 통과 소요 시간 : ' + str(elapsed_time), True, timer_text_color) # 타이머 위치 지정
                    screen.blit(final_timer, (screen_width*0.35, screen_height*0.01)) # 타이머 위치 지정
                    
                if home_button.draw():
                    main_menu = True
                    hard_level = 1
                    #reset hard_level
                    hard_world_data = []
                    world = reset_hard_level(hard_level)
                    game_over = 0
     
                elif restart_button.draw():
                    main_menu = 'hard'
                    start_ticks = pygame.time.get_ticks() #시작 시간 설정
                    total_time = hard_timer # hard_mode 시간 200초
                    hard_level = 1
                    #reset level
                    world_data = []
                    world = reset_hard_level(level)
                    game_over = 0
                

    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            run = False  # 닫히는 이벤트가 발생하였으면 게임이 진행중이 아님

    pygame.display.update()  # 게임 화면을 다시 그리기 ( 반드시 계속 호출되어야 함 )

pygame.quit()  # pygame 종료