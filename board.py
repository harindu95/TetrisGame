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
        self.next_block = None
        self.init()
        self.cleared_rows = 0
        self.end = False
        

    def draw(self, surface):
        self.draw_board(surface)
        self.block.draw(surface, self.block.col* column_width + self.x, self.block.row * column_width + self.y)
        for cell in self.cells:
            cell.draw(surface, cell.col* column_width + self.x, cell.row * column_width + self.y)

    def draw_board(self, surface):
        BLACK = (255,200,255)
        for i in range(number_columns+1):
            pygame.draw.aaline(surface, BLACK, (i* column_width + self.x, self.y), (i* column_width + self.x, column_width*number_rows + self.y))

        for i in range(number_rows +1):
            pygame.draw.aaline(surface, BLACK, (self.x, i*column_width + self.y),
            (column_width * number_columns + self.x, i*column_width + self.y))

    def init(self):
        if self.next_block == None:

            block_color = blocks.colors[randint(0, len(blocks.colors) -1)]
            block_type = randint(0, len(blocks.types) -1)
            start_col = randint(2, number_columns-2)
            self.next_block = blocks.Block(block_color, start_col,0, block_type)

        self.block = self.next_block
        block_color = blocks.colors[randint(0, len(blocks.colors) -1)]
        block_type = randint(0, len(blocks.types) -1)
        start_col = randint(2, number_columns-2)
        self.next_block = blocks.Block(block_color, start_col,0, block_type)

        if self.check_stop_moving(self.block):
            self.end = True

    def update_block(self, row=1, col=0, rotate=False):
        import copy
        if self.check_stop_moving(self.block):
            return
        prev_block = copy.deepcopy(self.block)
        self.block.col += col
        self.block.row += row
        if rotate :
            self.block.rotate()
        if not self.valid_block_state(self.block):
            self.block = prev_block

    def update(self, update=False):
        # if not self.block.moving:
            # self.init()
        if update:
            self.update_block()
        if self.check_stop_moving(self.block):
            self.cells += self.block.get_cells()
            self.init()
            self.clear_lines()

    def clear_lines(self):
        number_of_cells_per_row = [0 for x in range(number_rows)]
        for cell in self.cells:
            number_of_cells_per_row[cell.row] += 1

        filled_rows = [n for n in range(number_rows) if number_of_cells_per_row[n] >= number_columns]
        modified = self.cells
        for r in filled_rows:
            modified = [ c for c in modified if c.row != r]
            for c in self.cells:
                if c.row < r:
                    c.row += 1
        self.cells = modified
        self.cleared_rows += len(filled_rows)

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

    def handle_events(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.update_block(col=-1)
            elif e.key == pygame.K_RIGHT:
                self.update_block(col=1)
            elif e.key == pygame.K_DOWN:
                for i in range(5):
                    self.update_block()
            elif e.key == pygame.K_UP:
                self.update_block(rotate=True)
            elif e.key == pygame.K_SPACE:
                for x in range(number_rows):
                    self.update_block(row=1)
            # elif e.key == pygame.K_LEFT:
            #     self.block.rotate(False)



    def valid_block_state(self, block):
        for cell in block.cells:
            cell_col = cell.col + block.col
            cell_row = cell.row + block.row
            if cell_col >= number_columns or cell_col < 0:
                return False
            if cell_row >= number_rows :
                return False
            for c in self.cells:
                if c.col == cell.col and c.row == cell.row:
                    return False
        return True

