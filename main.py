from pygame_manager import MainManager
import constants as cns
import pygame as pg


def work_loop(main_manager):
    clock = pg.time.Clock()

    while True:
        main_manager.display()
        main_manager.update()
        clock.tick(500)

if __name__ == '__main__':
    mainManager = MainManager(cns.WIN_SIZE_MID)

    work_loop(mainManager)



