#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
import pygame

class Background(Entity):
    def _init_(self, name: str, position: tuple, size: tuple = None):
        super()._init_(name, position, size)

    def move(self):
        pass  # fundo fixo não precisa mover

    def draw(self, screen):
        if self.surf:
            screen.blit(self.surf, self.rect)