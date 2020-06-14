import pygame as pg
from tuple_operations import add_up, subtract


class CameraPositionController:

    def __init__(self, snowball_drawer):
        self.sbDrawer = snowball_drawer

        self.offset = (600, 400)
        self.line_size = 5

        self.mouse1 = (0, 0)
        self.mouse2 = (0, 0)
        self.change = False

    def check_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            self.mouse1 = pg.mouse.get_pos()
            self.change = True

        if event.type == pg.MOUSEMOTION:
            if self.change:
                self.mouse2 = pg.mouse.get_pos()
                diff = subtract(self.mouse2, self.mouse1)
                self.offset = add_up(self.offset, diff)
                self.mouse1 = self.mouse2
                self.sbDrawer.change_camera_position(self.offset, self.line_size)

        if event.type == pg.MOUSEBUTTONUP:
            self.change = False

            if event.button == 4:
                self.line_size += 1
            elif event.button == 5:
                self.line_size -= 1

            self.sbDrawer.change_camera_position(self.offset, self.line_size)