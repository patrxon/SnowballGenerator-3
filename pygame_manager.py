import pygame as pg
import sys

from snowball_drawer import SnowballDrawer
from line_manager import LineManager
from camera_position_controller import CameraPositionController
from sequence_translator import translate_sequence
from hud_drawer import HudDrawer
import constants as cns


class MainManager:
    def __init__(self, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)

        self.sbDrawer = SnowballDrawer(cns.DRAW_BOX_SIZE_MID, self.win)
        self.hudDrawer = HudDrawer(cns.DRAW_BOX_SIZE_MID, self.win)
        self.cameraController = CameraPositionController(self.sbDrawer)

        self.lnManager = LineManager()

        seq = [("j", 12), ("r", 2), ("l", 2)]
        tseq = translate_sequence(seq)
        self.lnManager.add_line((0, 0), (0, 1), tseq)

        self.lines = self.lnManager.get_lines()

        self.sbDrawer.draw_bg_box()

    def update(self):

        self.lnManager.iterate_lines()
        self.events()

    def display(self):

        self.sbDrawer.draw_snowball(self.lines)
        self.hudDrawer.draw_outer_box()

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            self.cameraController.check_event(event)
