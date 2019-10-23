#!/bin/python3
# Coding:Utf-8

import pygame

from labyrinth.const import *
from labyrinth.level import *

class Character():
    """ Mother class for characters """

    def __init__(self):
        self.alive = True
        self.x = 0
        self.y = 0
        self.pos = []

        self.png = None

    def set_position(self, pos):
        """ Initialise a position on map """

        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos

    def init_sprite(self, file):
        """ Load the img for display """

        self.png = pygame.image.load(file).convert_alpha()

    def display(self, Win):
        """ Display the character on win """

        #Convert X and Y for GUI
        gui_x = self.x * SPRITE_SIZE
        gui_y = self.y * SPRITE_SIZE

        self.pos = [self.x, self.y] #Line for test

        print("DISPLAY POS CHAR", self.pos)

        Win.blit(self.png, (gui_y, gui_x))

    def is_alive(self):
        """ Show if the character is still alive """

        return self.alive
    
    def pawned(self):
        """ Kill the character (life is unfair) """

        self.alive = False


class Hero(Character):
    """ Player class """

    def __init__(self):
        self.alive = True
        self.items = 0

    def can_kill(self):
        """ Tell if the player have enough items to kill the guard"""

        if self.items == 3:
            return True
        else:
            return False

    def move(self, Level, direction):
        """ Change the position of the character """

        new_pos = []

        #Verify that the position wanted is not a wall and move after
        if direction == 'up':
            if self.x > 0:
                if Level.what([self.x-1, self.y]) != '#':
                    self.x -= 1

        elif direction == 'down':
            if self.x < 14:
                if Level.what([self.x+1, self.y]) != '#':
                    self.x += 1

        elif direction == 'left':
            if self.y > 0:
                if Level.what([self.x, self.y-1]) != '#':
                    self.y -= 1

        elif direction == 'right':
            if self.y < 14:
                if Level.what([self.x, self.y+1]) != '#':
                    self.y += 1

        new_pos = [self.x, self.y]

        #Verify what event is at current position and return it
        if Level.find('N') == new_pos:
            Level.pick('N')
            self.items += 1
            print("ITEMS : ", self.items)
            return('N')

        elif Level.find('T') == new_pos:
            Level.pick('T')
            self.items += 1
            print("ITEMS : ", self.items)
            return('T')

        elif Level.find('E') == new_pos:
            Level.pick('E')
            self.items += 1
            print("ITEMS : ", self.items)
            return('E')


        elif Level.find('G') == new_pos:
            return ('G')

        #I don't know how to make a cool switch like in C++ :'(