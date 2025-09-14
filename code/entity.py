#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os
# print("Diretório atual:", os.getcwd())

from abc import ABC, abstractmethod
import pygame
import os


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.speed = 0

        # Tenta carregar a imagem se existir
        image_path = './asset/' + name + '.png'
        if os.path.isfile(image_path):
            self.surf = pygame.image.load(image_path)
            self.rect = self.surf.get_rect(left=position[0], top=position[1])
        else:
            # Se não existir, deixe para definir mais tarde
            self.surf = None
            self.rect = None

    @abstractmethod
    def move(self):
        pass

