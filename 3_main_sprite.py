import pygame

#기본 초기화(반드시 해야함)
pygame.init()

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sungmin Game!") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("/Users/sungminpark/PycharmProjects/pyGameTest2/background.jpg")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("/Users/sungminpark/PycharmProjects/pyGameTest2/character.jpg")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width // 2)  - (character_width // 2) # 화면 가로의 절반크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치


# 이벤트 루프
running = True
while running:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():

        # 2. 이벤트 처리(키보드, 마우스)
        if event.type == pygame.QUIT:
            running = False



    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시그리기!





#pygae 종료
pygame.quit()