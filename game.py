import pygame
from board import Board

class Game:

    def __init__(self, manager):
        self.board = Board(60,30)
        self.level = 1
        self.msElapsed = 0
        self.score = 0
        self.end = False
        self.manager = manager

    def draw(self, surface):
        self.board.draw(surface)
        self.display_info(surface)
        self.display_instructions(surface)

        if self.board.end:
            self.game_over(surface)

    def display_info(self, surface):
        myfont = pygame.font.SysFont("monospace", 24)
        label_color = (255,255,255)
        level_label = myfont.render("Level {}".format(self.level), 1, label_color)
        score_label = myfont.render("Score: {}".format(self.score), 1, label_color)
        surface.blit(level_label, (400, 100))
        surface.blit(score_label, (400, 200))
        pygame.draw.rect(surface, label_color, [400,300, 150, 150], 2)
        self.board.next_block.draw(surface, 445, 365)

    def display_instructions(self, surface):
        label_color = (255,255,255)
        instr_font = pygame.font.SysFont("monospace", 14)
        control_label = instr_font.render("Controls", 1, label_color)
        control_instr1 = instr_font.render("Up    - Rotate block", 1, label_color)
        control_instr2 = instr_font.render("Left  - Move left", 1, label_color)
        control_instr3 = instr_font.render("Right - Move right", 1, label_color)
        control_instr4 = instr_font.render("Space - Move to bottom", 1, label_color)
        control_instr5 = instr_font.render("Down - Move down", 1, label_color)
        surface.blit(control_label, (400, 500))
        surface.blit(control_instr1, (400, 520))
        surface.blit(control_instr2, (400, 540))
        surface.blit(control_instr3, (400, 560))
        surface.blit(control_instr4, (400, 580))
        surface.blit(control_instr5, (400, 600))

    def game_over(self, surface):
        s = pygame.Surface((600,700), pygame.SRCALPHA)   # per-pixel alpha
        s.fill((255,255,255,128))                         # notice the alpha value in the color
        surface.blit(s, (0,0))

        heading = pygame.font.SysFont("monospace", 45)
        heading2 = pygame.font.SysFont("monospace", 25)
        heading_color = (0,0,0)
        end_label = heading2.render("Score: {}".format(self.score), 1, heading_color)
        game_over = heading.render("Game Over", 1, heading_color)
        surface.blit(game_over, (150, 200))
        surface.blit(end_label, (180, 250))
        restart_label = heading2.render("Press enter to restart", 1 , heading_color)
        surface.blit(restart_label, (100, 400))

    def update(self, time):
        self.msElapsed += time
        if self.end:
            return
        if self.msElapsed >= (300-(self.level * 15)):
            self.board.update(True)
            self.msElapsed = 0
        self.board.update()
        self.level = max(int(self.board.cleared_rows / 5) , 1)
        self.score = self.board.cleared_rows * 10
        self.end = self.board.end

    def handle_events(self, event):
        if self.end:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.manager.show_start()
        else:
            self.board.handle_events(event)
