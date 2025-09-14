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

from code.Const import WIN_WIDTH, COLOR_GREEN, COLOR_PURPLE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window

        imagem_original = pygame.image.load('./asset/Menu.png')
        self.surf = pygame.transform.scale(imagem_original, (600, 480))
        self.rect = self.surf.get_rect(topleft=(0, 0))

    def run(self, MENU_OPTIONS=None, menu_option=0):  # menu_option com valor padrão
        if MENU_OPTIONS is None:
            MENU_OPTIONS = MENU_OPTION

        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            #Images
            self.window.blit(self.surf, self.rect)
            self.menu_text(50, text="Futuristic City", text_color=COLOR_GREEN, text_center_pos=((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTIONS)):
                y_pos = 200 + 35 * i
                if i == menu_option:
                    cor = COLOR_WHITE  # Destaque: branco
                else:
                    cor = COLOR_PURPLE  # Normal: roxo

                self.menu_text(20, text=MENU_OPTIONS[i], text_color=cor, text_center_pos=((WIN_WIDTH / 2), y_pos))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #down key
                        if menu_option < len(MENU_OPTIONS) - 1:
                            # menu_option = menu_option + 1
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #up key
                        if menu_option > 0:
                            # menu_option = menu_option + 1
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTIONS) - 1
                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]


            # pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)