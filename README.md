# 2022-2-OSSProj-Oneplusone-10


## 0️⃣ INFORMATION
## One plus one Team 1️⃣➕1️⃣
![Generic badge](https://img.shields.io/badge/license-MIT-green.svg)
![Generic badge](https://img.shields.io/badge/OS-ubuntu-red.svg)
![Generic badge](https://img.shields.io/badge/IDE-VSCode-green.svg)
![Generic badge](https://img.shields.io/badge/python-3-blue.svg)
![Generic badge](https://img.shields.io/badge/pygame-2.0.2-yellow.svg)
![Generic badge](https://img.shields.io/badge/pygame_menu-4.2.0-yellow.svg)

## 1️⃣ TEAM INTRODUCTION


### 팀명

원플러스원

### **팀원 구성**

| 신승원(팀장) | 산업시스템공학과 | 2018112481 |
| --- | --- | --- |
| 김규태(팀원) | 산업시스템공학과 | 2018112447 |
| 곽호은(팀원) | 경영정보학과 | 2020111571 |
| 민예지(팀원) | 경영정보학과 | 2020111571 |

## 2️⃣ PROJECT INTRODUCTION


### 1) 프로젝트 소개

안녕하세요 ☺️ 원플러스원 팀입니다!   
위의 게임은 pygame을 기반으로 하여 즐기는 platformer 게임입니다.  
동국대 마스코트 '아코'를 제한 시간 안에 과제물을 획득하게 하여 무사히 탈출 시키는 컨셉의 게임으로,  
EASY MODE, HARD MODE로 나누어 플레이가 가능합니다.  

## 3️⃣ HOW TO RUN


### **SETTING TO PLAY GAME**

```python
sudo apt-get update
sudo apt install python3-pip
sudo pip3 install pygame==2.0.2
sudo pip3 install pygame_menu==4.2.0
```

### **TO INSTALL THIS GAME**

```python
git clone https://github.com/CSID-DGU/2022-2-OSSProj-Oneplusone-10.git
cd 2022-2-OSSProj-Oneplusone-10
cd Platformer-master
```

### **TO RUN THIS GAME**

```python
python3 main.py
```

### 게임 시연 영상

유튜브 링크
https://youtu.be/sqyRi8oyK-A

## 4️⃣ HOW TO PLAY

### 메인 화면(화면을 늘이면 게임 룰이 보입니다.)

<img width="700" alt="스크린샷 2022-12-13 오후 8 51 52" src="https://user-images.githubusercontent.com/101270528/207310679-9a805096-d57c-4add-a48b-481513d5fdea.png">

**⓵ START**

- START 버튼 눌렀을 때 나오는 페이지

<img width="700" alt="스크린샷 2022-12-12 오전 12 43 21" src="https://user-images.githubusercontent.com/101270528/207310365-a9b44779-5cd7-4c92-b7b6-648a2015d7eb.png">


### 1) EASY MODE

EASY MODE 플레이 화면

![KakaoTalk_Photo_2022-12-13-23-45-33](https://user-images.githubusercontent.com/101270528/207365345-fb02fd8f-fb22-4125-86e5-0ae5050ed966.png)

제한시간 100초 / 과제물 20개를 획득해야 클리어 가능 

### 2) HARD MODE

HARD MODE 플레이 화면

![KakaoTalk_Photo_2022-12-13-23-45-39](https://user-images.githubusercontent.com/101270528/207365367-77b28e9c-1a44-48de-9452-bf8791f0162f.png)

제한시간 200초 / 과제물 40개를 획득해야 클리어 가능

**⓶ SKIN**

<img width="700" alt="스크린샷 2022-12-12 오전 12 43 16" src="https://user-images.githubusercontent.com/101270528/207310259-f5cc2d91-107e-4ea0-b9cf-67b84f1efc22.png">

해당 페이지에서는 게임 내에서 플레이 할 아코를 선택할 수 있습니다. Default 값은 기본 아코로 설정되어 있습니다.

**⓷ OPTION**

OPTION 메뉴에서는 게임 내 SOUND를 켜거나 끌 수 있으며, 게임 룰 페이지에서 게임 조작 방법을 익힐 수 있습니다.

- GAME RULE 페이지

<img width="700" alt="스크린샷 2022-12-13 오후 8 53 19" src="https://user-images.githubusercontent.com/101270528/207310918-07b6dcf6-f211-4c89-a883-7649b829d9af.png">

**⓸ EXIT**

EXIT 버튼 클릭 시, 게임이 종료됩니다.

## 5️⃣ **STRUCTURE**


1) **SYSTEM UI ARCHITECTURE**

<img width="466" alt="스크린샷 2022-12-13 오후 6 50 25" src="https://user-images.githubusercontent.com/101270528/207310117-915bceaa-fb37-4455-a000-aee275c97694.png">

**2) FILE STRUCTURE**

<img width="162" alt="스크린샷 2022-12-13 오후 8 24 18" src="https://user-images.githubusercontent.com/101270528/207308940-18a7bef8-deb9-412e-851b-52d9fd7e2737.png">

| analysis_code | 코드 분석 파일 |
| --- | --- |
| img | 게임에 필요한 모든 이미지 |
| level_data | EASY MODE, HARD MODE 각 맵별 데이터 |
| DungGeunMo.ttf, Puradak Gentle Gothic OTF.otf | 게임 실행에 필요한 폰트 |
| game_button.py | 게임 내 버튼 구현 |
| game_image_sound.py | 게임 내 sound on/off 구현 |
| game_rule.py | 게임 룰 페이지 |
| game_setting.py | 게임 세팅  |
| level_editor.py | 게임 내 이미지 로드, 이지모드, 하드모드 맵 구축을 위한 기본 정의 |
| main | 게임 실행 |

## 6️⃣ **SOURCE**


### REFERENCE

Game Source : [https://github.com/russs123/Platformer](https://github.com/russs123/Platformer)
