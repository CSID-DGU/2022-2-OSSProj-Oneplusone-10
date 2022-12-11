#타이머
fps = 60

#스크린 크기
screen_width = 1000
screen_height = 1000

#define game variables

# tile_size 관련
tile_size = 50
coin_tile_size = tile_size // 2

game_over = 0               # game over 일때를 0으로 설정
main_menu = True

# 이지모드 & 하드모드 레벨 설정  
level = 1
max_levels = 2
hard_level = 1
hard_max_levels = 5
 
score = 0
coin_score_text_x = tile_size - 10      # 코인 스코어 텍스트 x 좌표
coin_score_text_y = 10                  # 코인 스코어 텍스트 y 좌표
game_font_size = 30                     # game_font 사이즈 설정

start_height = screen_height - 130 # 캐릭터 초기 높이 

inplay_ako_size = (40, 80)              # 게임실행 할때 아코 사이즈
skin_ako_size = (200, 200)              # 스킨 페이지에서의 기본 아코 사이즈
skin_winter_ako_size = (220,220)        # 스킨 페이지에서의 겨울 아코 사이즈
skin_school_ako_size = (200,200)        # 스킨 페이지에서의 과잠 아코 사이즈
skin_graduation_ako_size = (200,200)    # 스킨 페이지에서의 졸업 아코 사이즈

background_coordinate = (0,0)       # 배경 이미지 위치 설정
timer_coordinate = (900,10)         # 게임 실행할때 타이머 위치 설정
timer_text_color = (255,255,255)    # 타이머 텍스트 색상 지정 -> 하얀색으로


easy_record = 1000    # 이지모드 기록 달성을 위한 변수
hard_record = 1000    # 하드모드 기록 달성을 위한 변수
easy_timer = 100      # 이지모드 제한시간 타이머 초기값
hard_timer = 200      # 하드모드 제한시간 타이머 초기값
game_over_time = 0    # 게임 진행 중 타이머가 0이 되면 게임 종료