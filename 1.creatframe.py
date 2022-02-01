import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")


#배경이미지 불러오기
background = pygame.image.load("C:/Users/ilrar/Python/pygame_basic/background.png")
#이벤트루프
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  
  #screen.fill((0,0,255))
  screen.blit(background, (0,0)) #배경그리기
#pygame 종료
  pygame.display.update() #게임화면을 다시 그리기


pygame.quit() #종료
