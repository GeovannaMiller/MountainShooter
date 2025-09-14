#!/usr/bin/python
# -*- coding: utf-8 -*-
# import pygame.image
#
# class Menu:
#     def __init__(self, window):
#         self.window = window
#         self.surf = pygame.image.load('./asset/Menu.png')
#         self.rect = self.surf.get_rect(left=0, top=0)
#
#     def run(self, ):
#         # self.window.blit(source=self.surf, dest=self.rect)
#         self.window.blit(self.surf, (0, 0))
#         pygame.display.flip()
#         pass

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_GREEN, COLOR_PURPLE, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window

        imagem_original = pygame.image.load('./asset/Menu.png')
        self.surf = pygame.transform.scale(imagem_original, (600, 480))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def run(self, MENU_OPTIONS=None):
        if MENU_OPTIONS is None:
            MENU_OPTIONS = MENU_OPTION

        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, text="Futuristic City", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTIONS)):
                # y_pos = 150 + i * 40
                self.menu_text(20, text=MENU_OPTIONS[i], text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 200 + 35 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)