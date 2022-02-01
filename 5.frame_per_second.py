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

#화면 주사율

ct = 60

#이벤트루프
running = True
while running:
  dt = clock.tick(ct) #게임화면의 초당 프레임수를 결정
  
  print("fps : " + str(clock.get_fps()))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.KEYDOWN:
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
    

  
  #screen.fill((0,0,255))
  screen.blit(background, (0,0)) #배경그리기
  
  screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
  
  pygame.display.update() #게임화면을 다시 그리기


pygame.quit() #종료
