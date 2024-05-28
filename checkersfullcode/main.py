
import pygame
from checkers.constant import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.board import board
from checkers.game import game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('checkers')

def get_row_col_from_mouse(pos):
  x,y = pos
  row = y//SQUARE_SIZE
  col = x // SQUARE_SIZE
  return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    Game = game(WIN)

    while run :
      clock.tick(FPS)

      if Game.turn == WHITE:
        value, new_board = minimax(Game.get_board(), 3, WHITE, Game)
        Game.ai_move(new_board)

      if Game.winner() != None:
        print (Game.winner())
        run = False
       
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
          pos = pygame.mouse.get_pos()
          row, col = get_row_col_from_mouse(pos)
          Game.select(row,col) 

      Game.update()
      pygame.display.update()    
    pygame.quit()
main()    