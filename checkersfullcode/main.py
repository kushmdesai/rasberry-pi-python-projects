
import pygame
from checkers.constant import WIDTH, HEIGHT
from checkers.board import board

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    gboard = board()

    while run :
      clock.tick(FPS)
       
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
         pass
      gboard.draw(WIN)
      pygame.display.update()    
    pygame.quit()
main()    