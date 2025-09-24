import pygame as pg

class PG:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        self.clock = pg.time.Clock()
        self.running = True
        self.fps = 60
        