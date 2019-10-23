#!/bin/python3
# Coding:Utf-8

import pygame
from pygame.locals import *

from labyrinth.const import *
from labyrinth.level import *

class Items():
    """ item class """

    def __init__(self):
        self.available = True
        self.x = 0
        self.y = 0
        self.png = None

    def set_position(self, pos):
        """ Set the original position """

        self.x = pos[0]
        self.y = pos[1]

    def init_sprite(self, file):
        """ load png sprite """

        self.png = pygame.image.load(file).convert_alpha()

    def display(self, Win):
        """ Display the sprite on win """

        #convert X and Y to GUI
        gui_x = self.x * SPRITE_SIZE
        gui_y = self.y * SPRITE_SIZE

        Win.blit(self.png, (gui_y, gui_x))

    def picked(self):
        """ Disable the item """

        self.available = False

    def is_available(self):
        """ Tell if the  item is available """
        return self.available
