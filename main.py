import pygame
import manager

game = manager.Manager()

def draw(surface):
    BLACK = (30, 30, 30)
    surface.fill(BLACK)
    game.draw(surface)
    pygame.display.update()

def main():
    pygame.init()
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((600,700))
    running = True
    clock = pygame.time.Clock()
    msElapesd = 0
    while running:
        msElapesd = clock.tick(60)
        draw(screen)
        game.update(msElapesd)
        # event handling , gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            else:
                game.handle_events(event)
    
if __name__=="__main__":
    main()
