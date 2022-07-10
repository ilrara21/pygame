import pygame


pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#r게임 이름 정하기
pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()


#배경이미지 불러오기
background = pygame.image.load("/Users/ilrara/Dev/pygame_basic/background.png")

#메인캐릭터 불러오기
character = pygame.image.load("/Users/ilrara/Dev/pygame_basic/char1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ((screen_width) -(character_width))/2
character_y_pos = screen_height-character_height

#이동할 좌표
to_x = 0
to_y = 0

#이동속도

character_speed = 0.4

# 적 enemy  캐릭터

enemy = pygame.image.load("/Users/ilrara/Dev/pygame_basic/enemy1.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1] #캐릭터의 세로크기
enemy_x_pos = (screen_width /2) - (enemy_width /2) # 화면 가로의 절반 크기에 
enemy_y_pos = (screen_height /2) -(enemy_height /2)  # 화면 세로 크기 가장 아래에 해당하는  곳에 위치

#화면 주사율

ct = 60

#폰트정의
game_font = pygame.font.Font(None, 40) #폰트 객제 생성(폰트, 크기)

#총시간
total_time = 10

#시작 시간 정보

start_ticks = pygame.time.get_ticks()#시작 tick 정보를 받아옴

#이벤트루프
running = True #게입이 진행중인가?
while running:
  dt = clock.tick(ct) #게임화면의 초당 프레임수를 결정

  print("fps : " + str(clock.get_fps()))
  
  for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
        running = False
      
    if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
        if event.key == pygame.K_LEFT:
          to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
          to_x += character_speed
        elif event.key == pygame.K_UP:
          to_y -= character_speed
        elif event.key == pygame.K_DOWN:
          to_y += character_speed
          
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          to_x = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
          to_y = 0

          
  character_x_pos += to_x*dt
  character_y_pos += to_y*dt
  
  
  # 가로 경계값 처리
  if character_x_pos < 0:
      character_x_pos = 0
  elif character_x_pos > screen_width - character_width:
      character_x_pos = screen_width - character_width    
      
  #세로 경계값 처리
  if character_y_pos < 0:
    character_y_pos = 0
  elif character_y_pos > screen_height - character_height :
    character_y_pos = screen_height - character_height

#충돌처리

  character_rect = character.get_rect()
  character_rect.left = character_x_pos
  character_rect.top = character_y_pos

  enemy_rect = enemy.get_rect()
  enemy_rect.left = enemy_x_pos
  enemy_rect.top = enemy_y_pos

#충돌체크

  if character_rect.colliderect(enemy_rect):
    print ("충돌했어요")
    running = False


  
  #screen.fill((0,0,255))
  screen.blit(background, (0,0)) #배경그리기
  
  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
  screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기


  #타이머 집어넣기
  #경과 시간 계산
  elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 #경과시간을 1000으로 나누어서 초단위로 표시

  timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255)) #출력할 글짜, true, 글 색상

  screen.blit(timer, (10,10))

  if total_time - elapsed_time <= 0:
    print("타임아웃")
    running = False

  pygame.display.update()

pygame.time.delay(2000) #2초 정도 대기

pygame.quit() #종료