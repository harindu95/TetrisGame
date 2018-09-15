import pygame
import os


play_btn_bg = (20,50,80)
play_btn_bg_focus = (30, 60, 90)

class StartPage:

    def __init__(self, manager):
        self.play_btn_color = play_btn_bg
        self.manager = manager

    def draw(self, surface):
        myimage = pygame.image.load(os.path.join("background.png"))
        imagerect = myimage.get_rect()
        surface.blit(myimage, imagerect)

        font = pygame.font.SysFont("monospace", 72)
        text_color = (50, 30, 20)
        title = font.render("Tetris" , 1, text_color)
        surface.blit(title, (200,200))


        pygame.draw.rect(surface, self.play_btn_color, [225,400, 150, 50])
        play_color = (225,225, 225)
        play_font = pygame.font.SysFont("monospace", 42)
        play = play_font.render("Play" , 1, play_color)
        surface.blit(play, (250,400))

    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        button = pygame.Rect(225, 400, 150, 50)
        if button.collidepoint(mouse_pos):
            self.play_btn_color = play_btn_bg_focus
            if event.type == pygame.MOUSEBUTTONDOWN :
                self.manager.show_game()
        else:
            self.play_btn_color = play_btn_bg

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.manager.show_game()

    def update(self, time):
        pass
