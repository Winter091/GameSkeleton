import pygame as pg
from Game.MenuManager import MenuManager
from Game.Const import WINDOW_W, WINDOW_H


class Core(object):
    def __init__(self):
        pg.mixer.pre_init(44100, -16, 2, 1024)
        pg.init()

        self.oMM = MenuManager()
        self.screen = pg.display.set_mode((WINDOW_W, WINDOW_H))
        self.running = True
        self.keys = [False] * 512

    def main_loop(self):
        while self.running:
            self.input()
            self.update()
            self.render()

    def input(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.running = False

            elif e.type == pg.KEYDOWN:
                self.keys[e.key] = True

            elif e.type == pg.KEYUP:
                self.keys[e.key] = False

    def update(self):
        pass

    def render(self):
        pass
