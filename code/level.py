#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.const import WIN_WIDTH, WIN_HEIGHT, FPS, COLOR_BLACK

class Level:
    def _init_(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # cria um fundo ajustado ao tamanho da tela
        bg = EntityFactory.create_background("Level1Bg", (0, 0), size=(WIN_WIDTH, WIN_HEIGHT))
        self.entity_list.append(bg)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.window.fill(COLOR_BLACK)

            for ent in self.entity_list:
                if ent.surf:
                    self.window.blit(ent.surf, ent.rect)

            pygame.display.flip()
            clock.tick(FPS)
