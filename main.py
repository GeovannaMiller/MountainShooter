import pygame

from code.game import Game

pygame.init()
pygame.mixer.init()

game = Game()
game.run()


