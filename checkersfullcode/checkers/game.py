import pygame
from .constant import RED, WHITE, BLUE, SQUARE_SIZE
from checkers.board import board

class game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win) 
        self.draw_valid_moves(self.valid_moves)  
        pygame.display.update()

    def _init(self):
        self.seleccted=None
        self.board = board()
        self.turn = RED
        self.valid_moves = {}
    
    def reset(self):
        self._init()

    def select(self,row,col):
        if self.seleccted:
            result = self._move(row,col)
            if not result:
                self.seleccted = None
                self.select(row,col)

        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
            self.seleccted = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False

    def _move(self,row,col):
        piece = self.board.get_piece(row,col)
        if self.seleccted and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.seleccted, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()                
        else:
            return False
        return True
    
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED    

    def winner(self):
        return self.board.winner()

    def get_board(self):
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.change_turn()