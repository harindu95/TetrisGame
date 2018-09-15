from game import Game
from start import StartPage

class Manager:

    def __init__(self):
        self.start = StartPage(self)
        self.page = self.start

    def draw(self, surface):
        self.page.draw(surface)

    def update(self, time):
        self.page.update(time)

    def handle_events(self, event):
        self.page.handle_events(event)

    def show_game(self):
        self.page = Game(self)

    def show_start(self):
        self.page = self.start
