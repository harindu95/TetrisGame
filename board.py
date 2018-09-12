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
        self.msElapsed = 0
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
        block_type = randint(0, len(blocks.types) -1)
        start_col = randint(0, number_columns)
        self.block = blocks.Block(block_color, start_col,0, block_type)

        while not self.valid_block_state(self.block):
            start_col = randint(0, number_columns)
            self.block = blocks.Block(block_color, start_col,0, block_type)

    def update(self):
        import copy
        self.msElapsed += self.clock.tick(30)
        prev_block = copy.deepcopy(self.block)
        # if not self.block.moving:
            # self.init()
        if self.msElapsed >= 300:
            self.block.update()
            self.msElapsed = 0
        if self.check_stop_moving(self.block):
            self.cells += self.block.get_cells()
            self.init()
            self.clear_lines()
        elif not self.valid_block_state(self.block):
            self.block = prev_block

    def clear_lines(self):
        number_of_cells_per_row = [0 for x in range(number_rows)]
        for cell in self.cells:
            number_of_cells_per_row[cell.row] += 1
        for n in number_of_cells_per_row:
            if n == number_columns:
                modified = [c for c in self.cells if c.col != n]
                self.cells = modified

    def check_stop_moving(self, block):
        for cell in block.cells:
            cell_col = cell.col + block.col
            cell_row = cell.row + block.row
            for stableCell in self.cells:
                if cell_col == stableCell.col and cell_row == (stableCell.row - 1):
                    return True
            if cell_row == (number_rows - 1):
                return True
        return False

    def handle_keyboard(self, e):
        import copy
        prev_block = copy.deepcopy(self.block)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.block.col -= 1
            elif e.key == pygame.K_RIGHT:
                self.block.col += 1
            elif e.key == pygame.K_DOWN:
                self.block.row += 5
        if not self.valid_block_state(self.block):
            self.block = prev_block


    def valid_block_state(self, block):
        for cell in block.cells:
            cell_col = cell.col + block.col
            cell_row = cell.row + block.row
            if cell_col >= number_columns or cell_col < 0:
                return False
            if cell_row >= number_rows :
                return False
        return True

