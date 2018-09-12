import pygame
import blocks
import board

board = board.Board(60,30)
def draw(surface):
    BLACK = (30, 100, 0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)
    surface.fill(WHITE)
     # This draws a triangle using the polygon command
    board.draw(surface)
    pygame.display.update()

def main():
    
    pygame.init()
    pygame.display.set_caption("Tetris")
    
    screen = pygame.display.set_mode((600,800))
    
    running = True
    # main loop
    while running:
        draw(screen)
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            else:
                board.handle_keyboard(event)
    
if __name__=="__main__":
    main()
