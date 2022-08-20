from msilib import change_sequence
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

# 📍 배경 이미지 불러오기
background = pygame.image.load(
    "/python_projects/pygame_basic/background.png")

# 📍 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "/python_projects/pygame_basic/character.png")
character_size = character.get_rect().size  # 이미지의 크기를 리스트형태로 구해옴
character_width = character_size[0]  # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
# 👇 화면가로의 절반크기에 해당하는 곳에 위치 (가로위치)
character_x_pos = (screen_width-character_width) / 2
# 👇 화면 세로 크기의 가장 아래에 해당하는 곳에 위치 (세로위치)
character_y_pos = screen_height-character_height

# 📍 이벤트 루프
running = True  # 게임이 진행중인가?
while(running):
    # 어떤 이벤트가 발생하였는가?
    for event in pygame.event.get():  # pygame을 쓰려면 무조건 써야하는 코드!
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트(닫기버튼)가 발생하였는가?
            running = False  # 게임이 진행중이 아님

    screen.blit(background, (0, 0))  # 배경 그리기
    # 👆 이렇게 하는 것 대신에 👇아래처럼 RGB로 채울 수 있다
    # screen.fill((0, 100, 255))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 게임화면을 다시 그리기 (반드시 계속 호출되어야 하는 부분!!)
    # 👆 pygame에서는 매 frame마다 화면을 새로 그려주는 동작을 해줘야함!
    #   : 이걸 해줘야지 while구문을 계속 돌면서 화면을 계속 그려줌


# 📍 pygame 종료
pygame.quit()
