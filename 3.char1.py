import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("My Game")


#배경이미지 불러오기
background = pygame.image.load("C:/Users/ilrar/Python/pygame_basic/background.png")

#메인캐릭터 불러오기
character = pygame.image.load("C:/Users/ilrar/Python/pygame_basic/char1.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = ((screen_width) -(character_width))/2
character_y_pos = screen_height-character_height


#이벤트루프
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  
  #screen.fill((0,0,255))
  screen.blit(background, (0,0)) #배경그리기
  screen.blit(character, (character_x_pos,character_y_pos))#pygame 종료
  pygame.display.update() #게임화면을 다시 그리기


pygame.quit() #종료
