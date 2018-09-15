import pygame

colors = [(9, 132, 227, 1.0),
          (214, 48, 49, 1.0),
          (253, 203, 110, 1.0),
          (0, 184, 148, 1.0),
          (232, 67, 147, 1.0),
          (108, 92, 231, 1.0) ]

types = [
    {
        'rotate':True,
        'units' : [
            {'x' : 0, 'y' : 0}
        ]
    },
    {
        'rotate' : True,
        'units' : [
            {'x' : 0, 'y' : 0},
            {'x' : 0, 'y' : 1},
            {'x' : 0, 'y' : -1}
        ]
    },
    {
        'rotate' : True,
        'units' : [
            {'x' : 1, 'y' : 1},
            {'x' : 0, 'y' : 1},
            {'x' : 0, 'y' : 0},
            {'x' : 0, 'y' : -1}
            ]
    },
    {
        'rotate' : True,
        'units' : [
            {'x' : 0, 'y' : -1},
            {'x' : 0, 'y' : 0},
            {'x' : -1, 'y' : 0},
            {'x' : 1, 'y' : -1}
        ]
    },
    {
        'rotate' : True,
        'units' : [
            {'x' : 0, 'y' : -1},
            {'x' : 0, 'y' : 0},
            {'x' : 1, 'y' : 0},
            {'x' : -1, 'y' : -1}
        ]
    },
    {
        'rotate' : False,
        'units' : [
            {'x' : 1, 'y' : 1},
            {'x' : 0, 'y' : 1},
            {'x' : 0, 'y' : 0},
            {'x' : 1, 'y' : 0}
        ]
    }
]


class Cell:

    def __init__(self, col, row, color, size):
        self.color = color
        self.size = size
        self.col = col
        self.row = row

    def draw(self, surface, x, y):
        BORDER = (0,0,0)
        pygame.draw.rect(surface, self.color, [x,y, self.size, self.size])
        pygame.draw.rect(surface, BORDER, [x,y, self.size, self.size], 2)


class Block:

    def __init__(self, color, col, row, type=2):
        self.type = type
        self.color = color
        self.col = col
        self.row = row
        self.moving = True
        self.initialize()

    def initialize(self):
        self.cells = []
        for c in types[self.type]['units']:
            self.cells.append(Cell(c['x'], c['y'], self.color, 30))

    def draw(self, surface, x, y):
        for cell in self.cells:
            cell_x = x + cell.col * cell.size
            cell_y = y + cell.row * cell.size
            cell.draw(surface, cell_x, cell_y)

    def rotate(self, clockwise=True):
        if clockwise:
            cos = 0
            sin = -1
        else:
            cos = 0
            sin = 1
        for cell in self.cells:
            x = cell.col * cos - cell.row * sin
            y = cell.col * sin + cell.row * cos
            cell.col = x
            cell.row = y

    def update(self):
        if(self.moving):
            self.row += 1

    def get_cells(self):
        cells = []
        for cell in self.cells:
            c = Cell(cell.col + self.col, cell.row + self.row, self.color, 30)
            cells.append(c)
        return cells
