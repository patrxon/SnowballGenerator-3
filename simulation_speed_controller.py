import pygame as pg


class SimulationSpeedController:

    def __init__(self, line_manager, hud_drawer):
        self.lnManager = line_manager
        self.hudDrawer = hud_drawer

        self.game_speed = 0
        self.iterate = True

    def updated_speed(self):
        if self.game_speed < 0:
            self.game_speed = 0

        counter = 2 ** self.game_speed
        self.lnManager.change_speed(counter, self.iterate)
        self.hudDrawer.change_speed(self.game_speed, self.iterate)

    def check_event(self, event):

        if event.type == pg.KEYDOWN:
            if event.key == 276:
                self.game_speed -= 1
            elif event.key == 275:
                self.game_speed += 1
            elif event.key == 32:
                self.iterate = not self.iterate

        self.updated_speed()
