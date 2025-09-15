#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os
# print("Diretório atual:", os.getcwd())

from abc import ABC, abstractmethod
import pygame
import os
from code.const import ASSET_DIR


class Entity(ABC):
    def _init_(self, name: str, position: tuple, size: tuple = None):
        self.name = name
        self.speed = 0

        image_path = os.path.join(ASSET_DIR, name + '.png')
        if os.path.isfile(image_path):
            self.surf = pygame.image.load(image_path).convert_alpha()
            if size:
                self.surf = pygame.transform.scale(self.surf, size)
            self.rect = self.surf.get_rect(topleft=position)
        else:
            self.surf = None
            self.rect = None

    @abstractmethod
    def move(self):
        pass