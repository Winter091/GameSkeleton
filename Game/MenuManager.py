import pygame as pg


class MenuManager(object):
    def __init__(self):
        self.currentGameState = None

    def update(self, core):
        if self.get_game_state() == 'MainMenu':
            pass
        elif self.get_game_state() == 'Loading':
            pass
        elif self.get_game_state() == 'Pause':
            pass
        elif self.get_game_state() == 'Game':
            pass

    def render(self, core):
        if self.get_game_state() == 'MainMenu':
            pass
        elif self.get_game_state() == 'Loading':
            pass
        elif self.get_game_state() == 'Pause':
            pass
        elif self.get_game_state() == 'Game':
            pass
        pg.display.update()

    def get_game_state(self):
        return self.currentGameState
