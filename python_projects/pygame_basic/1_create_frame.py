import pygame

pygame.init()  # 초기화 (반드시 필요)


# 📍 화면 크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))


# 📍 화면 타이틀 설정
pygame.display.set_caption("Nado Game")
# 👆 여기까지만 실행하면 화면이 나오려다 말고 꺼지는데,
# 1.사용자가 키를 입력하거나
# 2.마우스를 움직이는 등의
# 동작을 계속 검사하는 이벤트 루프가 항상 실행이 되어 있어야 창이 꺼지지 않는다!
# -> "이벤트 루프"로 ㄱㄱ


# 📍 이벤트 루프
running = True  # 게임이 진행중인가?
while(running):
    # 어떤 이벤트가 발생하였는가?
    for event in pygame.event.get():  # pygame을 쓰려면 무조건 써야하는 코드!
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트(닫기버튼)가 발생하였는가?
            running = False  # 게임이 진행중이 아님


# 📍 pygame 종료
pygame.quit()
