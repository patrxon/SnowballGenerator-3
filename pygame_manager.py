import pygame as pg
import sys

from snowball_drawer import SnowballDrawer
from line_manager import LineManager
from tuple_operations import add_up, subtract
from sequence_translator import translate_sequence
from hud_drawer import HudDrawer
import constants as cns


class MainManager:
    def __init__(self, fps, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)
        self.fps = fps

        self.sbDrawer = SnowballDrawer(cns.DRAW_BOX_SIZE_MID, self.win)
        self.hudDrawer = HudDrawer(cns.DRAW_BOX_SIZE_MID, self.win)

        self.lnManager = LineManager()

        seq1 = ({"r": 6, "l": 1})
        tseq1 = translate_sequence(seq1)

        self.lnManager.add_line((0, 0), (0, 1), tseq1)

        self.lines = self.lnManager.get_lines()

        self.offset = (600, 400)
        self.mouse1 = (0, 0)
        self.mouse2 = (0, 0)
        self.change = False
        self.line_size = 5
        self.sbDrawer.draw_bg_box()
        self.work_loop()

    def work_loop(self):
        clock = pg.time.Clock()

        while True:
            self.display()
            self.events()
            self.update()
            clock.tick(self.fps)

    def update(self):
        self.lnManager.iterate_lines()

    def display(self):

        self.sbDrawer.draw_snowball(self.offset, self.lines, self.line_size)
        self.hudDrawer.draw_outer_box()

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                self.mouse1 = pg.mouse.get_pos()
                self.change = True
            if event.type == pg.MOUSEMOTION:
                if self.change:
                    self.mouse2 = pg.mouse.get_pos()
                    diff = subtract(self.mouse2, self.mouse1)
                    self.offset = add_up(self.offset, diff)
                    self.mouse1 = self.mouse2
                    self.sbDrawer.refresh_draw()

            if event.type == pg.MOUSEBUTTONUP:
                self.change = False

                if event.button == 4:
                    self.line_size += 1
                elif event.button == 5:
                    self.line_size -= 1
