import pygame
import blocks
from random import randint

number_columns = 10
number_rows = 20
column_width = 30


class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cells = []
        self.block = None
        self.init()
        self.clock = pygame.time.Clock()

    def draw(self, surface):
        self.block.draw(surface, self.block.col* column_width + self.x, self.block.row * column_width + self.y)
        for cell in self.cells:
            cell.draw(surface, cell.col* column_width + self.x, cell.row * column_width + self.y)
        self.draw_board(surface)
        self.update()

    def draw_board(self, surface):
        BLACK = (0,0,0)
        for i in range(number_columns+1):
            pygame.draw.line(surface, BLACK, (i* column_width + self.x, self.y), (i* column_width + self.x, column_width*number_rows + self.y))

        for i in range(number_rows +1):
            pygame.draw.line(surface, BLACK, (self.x, i*column_width + self.y),
            (column_width * number_columns + self.x, i*column_width + self.y))

    def init(self):
        block_color = blocks.colors[randint(0, len(blocks.colors) -1)]
        while self.block is None or self.valid_block_state(self.block):
            start_col = randint(0, number_columns)
            self.block = blocks.Block(block_color, start_col, 0)

    def update(self):
        import copy
        msElapsed = self.clock.tick(5)
        prev_block = copy.deepcopy(self.block)
        if(msElapsed >= 30):
            self.block.update()
        blockValid = self.valid_block_state(self.block)
        if not blockValid:
            self.block = prev_block

    def valid_block_state(self, block):
        for cell in block.cells:
            cell_col = cell.col + block.col
            cell_row = cell.row + block.row
            if cell_col >= number_columns or cell_col < 0:
                return False
            if cell_row >= number_rows or cell_row < 0:
                return False
        return True
