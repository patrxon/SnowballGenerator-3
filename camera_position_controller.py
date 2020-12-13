import pygame as pg
from tuple_operations import add_up, subtract, divide, multiple


class CameraPositionController:

    def __init__(self, snowball_drawer):
        self.sbDrawer = snowball_drawer

        self.offset = (600, 400)
        self.line_size = 5

        self.mouse1 = (0, 0)
        self.mouse2 = (0, 0)
        self.change = False

    def control_offset(self):
        self.mouse2 = pg.mouse.get_pos()
        diff = subtract(self.mouse2, self.mouse1)
        self.offset = add_up(self.offset, diff)
        self.mouse1 = self.mouse2
        self.sbDrawer.change_camera_position(self.offset, self.line_size)

    def control_scroll(self, direction):

        mouse_pos = pg.mouse.get_pos()

        diff = subtract(self.offset, mouse_pos)
        if self.line_size != 0:
            diff = divide(diff, self.line_size)
            diff = multiple(diff, direction)

        self.offset = add_up(self.offset, diff)

        self.line_size += direction
        self.sbDrawer.change_camera_position(self.offset, self.line_size)

    def check_event(self, event):

        if event.type == pg.MOUSEBUTTONDOWN:
            self.mouse1 = pg.mouse.get_pos()
            self.change = True

        if event.type == pg.MOUSEMOTION:
            if self.change:
                self.control_offset()

        if event.type == pg.MOUSEBUTTONUP:
            self.change = False

            if event.button == 4:
                self.control_scroll(1)
            elif event.button == 5:
                self.control_scroll(-1)

            self.sbDrawer.change_camera_position(self.offset, self.line_size)
