import pygame as pg

input_list = "jlrg/0123456789"


class InputBox:

    def __init__(self, x, y, w, h, color=(250, 250, 250), text=''):
        self.x = x
        self.pointer = pg.Rect(x, y + h - 4, 0, 2)
        self.rect = pg.Rect(x, y, w, h)
        self.color = (0, 0, 0)
        self.text = text
        self.font = pg.font.Font(None, 32)
        self.txt_surface = self.font.render(text, True, self.color)
        self.color = color
        self.selected = -1
        self.hold = False
        self.event = ''

    def update_pointer(self):

        txt_aft = self.font.render(self.text[0:self.selected + 1], True, self.color)
        txt_pre = self.font.render(self.text[0:self.selected], True, self.color)

        height = txt_aft.get_width()
        height_left = txt_pre.get_width()

        self.pointer.w = height - height_left
        self.pointer.x = self.x + height_left + 5

    def change_select(self, direction):

        self.selected += direction

        if self.selected >= len(self.text):
            self.selected = len(self.text) - 1
        if self.selected < 0:
            self.selected = 0

    def handle_event(self, event):

        if event.type == pg.KEYDOWN:
            self.event = event.key
            self.hold = True
            if event.key == pg.K_BACKSPACE:
                self.text = self.text[0:self.selected] + self.text[self.selected + 1:]
                if self.selected > -1:
                    self.selected -= 1
            elif event.key == pg.K_LEFT:
                self.change_select(-1)
            elif event.key == pg.K_RIGHT:
                self.change_select(1)
            elif event.key == pg.K_UP:
                self.change_select(5)
            elif event.key == pg.K_DOWN:
                self.change_select(-5)
            elif event.key == pg.K_ESCAPE:
                self.text = ""
                self.selected = -1
            elif event.key == pg.K_c:
                self.text += self.text
            elif pg.key.name(event.key) in input_list:
                self.text = self.text[0:self.selected + 1] + event.unicode + self.text[self.selected + 1:]
                self.selected += 1

            if len(self.text) > 0:
                self.update_pointer()

            self.txt_surface = self.font.render(self.text, True, self.color)
            self.update()

        if event.type == pg.KEYUP:
            self.hold = False

    def get_text(self):
        return self.text

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        if len(self.text) > 0:
            pg.draw.rect(screen, self.color, self.pointer)

        pg.draw.rect(screen, self.color, self.rect, 2)
