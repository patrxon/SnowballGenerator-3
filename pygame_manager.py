import pygame as pg
import sys

from snowball_drawer import SnowballDrawer
from line_manager import LineManager
from camera_position_controller import CameraPositionController
from simulation_speed_controller import SimulationSpeedController
from sequence_translator import translate_sequence
from hud_drawer import HudDrawer
from text_box import InputBox

import constants as cns


class MainManager:
    def __init__(self, size):
        pg.init()
        self.size = size
        self.win = pg.display.set_mode(self.size)

        self.sbDrawer = SnowballDrawer(cns.DRAW_BOX_SIZE_MID, self.win)
        self.hudDrawer = HudDrawer(cns.DRAW_BOX_SIZE_MID, self.win)
        self.lnManager = LineManager()

        self.cameraController = CameraPositionController(self.sbDrawer)
        self.simulationController = SimulationSpeedController(self.lnManager, self.hudDrawer)

        self.inputBox = InputBox(100, 5, 500, 32)

        self.restart_simulation("r 1")

        self.sbDrawer.draw_bg_box()

    def restart_simulation(self, text):

        tab = text.split(' ')
        seq = []

        for i in range(int(len(tab) / 2)):
            seq += [(tab[2 * i], int(tab[2 * i + 1]))]

        tseq = translate_sequence(seq)

        self.lnManager.restart_lines()
        self.lnManager.add_line((0, 0), (0, 1), tseq)

        self.lines = self.lnManager.get_lines()

    def update(self):
        self.lnManager.iterate_lines()
        self.events()

    def display(self):
        self.sbDrawer.draw_snowball(self.lines)
        self.hudDrawer.draw_hud()
        self.inputBox.draw(self.win)

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    new_patter = self.inputBox.get_text()
                    self.restart_simulation(new_patter)

            self.inputBox.handle_event(event)
            self.cameraController.check_event(event)
            self.simulationController.check_event(event)
