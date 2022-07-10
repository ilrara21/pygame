import pygame

########################################################################
#기본 초기화 (반드시 해야 하는 것들)
pygame.init() 

#화면 크기 설정

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#r게임 이름 정하기
pygame.display.set_caption("My Game")

#FPS
clock = pygame.time.Clock()

###########################################################3


#1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 속도, 폰트 등 )


running = True #게입이 진행중인가?
while running:
  dt = clock.tick(60) #게임화면의 초당 프레임수를 결정


# 2. 이벤트 처리 (키보드, 마우스 등) 

  for event in pygame.event.get(): #어떤 이벤트가 발생하였는가?
    if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가?
        running = False
      
  
#3. 게임 캐릭터 위치 정의   
  

#4. 충돌처리
  

#5. 화면에 그리기


  pygame.display.update()

pygame.time.delay(1000) #2초 정도 대기

pygame.quit() #종료