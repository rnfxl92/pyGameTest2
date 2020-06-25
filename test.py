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



# 이벤트 루프
running = True
while running:
    # 1) 사용자 입력 처리
    for event in pygame.event.get():

        # 2. 이벤트 처리(키보드, 마우스)
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) #배경 그리기

    pygame.display.update() # 게임화면 다시그리기!





#pygae 종료
pygame.quit()