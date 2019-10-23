#!/bin/python3
# Coding:Utf-8

import pygame
from random import randint

from labyrinth.const import *

from random import randint

def spawner():
    """ Randomize 3 numbers for the item's spawns """

    spawn = [0, 0, 0] #0 = needle, 1 = Tube, 2 = Ether

    spawn[0] = randint(1, SPAWN)
    spawn[1] = randint(1, SPAWN)
    spawn[2] = randint(1, SPAWN)
    #if there is a double, so it randomize again

    while spawn[0] == spawn[1]:
        spawn[0] = randint(1, SPAWN)
        spawn[1] = randint(1, SPAWN)

    while spawn[1] == spawn[2] or spawn[2] == spawn[0]:
        spawn[2] = randint(1, SPAWN)

    return spawn

class Level():
    """Class for the level of the game."""

    def __init__(self):
        self.struct = [] #structure for the level

    def make(self):
        """ Generate the map in struct from source map txt file """
        with open(MAP, 'r') as file:
            struct_level = []

            for line in file:
                #slicing for each lines in txt
                line_level = []

                for case in line:
                    #slicing for each chars in line (cases)
                    if case != '\n':
                        line_level.append(case) #add the char to struct
                
                struct_level.append(line_level) #add the line to struct

            #save the result in struct
            self.struct = struct_level

    def display(self, Win):
        """ Display the background and walls """

        #load background and walls img
        background = pygame.image.load(BACKGROUND_IMG).convert()
        wall = pygame.image.load(WALL).convert()

        #add the bg
        Win.blit(background, (0, 0))

        i_line = 0
        #slicing, same as the make method but for blitting wall sprites
        for line in self.struct:
            i_case = 0

            for case in line:
                x = i_line * SPRITE_SIZE #set the gui position for X
                y = i_case * SPRITE_SIZE #set the gui position for Y

                if case == '#': #symbol for wall, for clarity in level creation
                    Win.blit(wall, (y, x))
                    #Y AND X NEED TO BE REVERSED WITH PYGAME BLIT !

                i_case += 1
            i_line += 1

    def init_spawn(self):
        """ initialise the spawn for items """

        spawn = spawner()
        print("spawn : ", spawn)
        count_S = 1 #count the number of S met yet for matching with spawn

        i_line = 0
        for line in self.struct:
            i_case = 0

            for case in line:
                if case == 'S': #symbol for a possible spawner on the map
                    if spawn[0] == count_S:
                        self.struct[i_line][i_case] = 'N' #Needle
                    elif spawn[1] == count_S:
                        self.struct[i_line][i_case] = 'T' #Tube
                    elif spawn[2] == count_S:
                        self.struct[i_line][i_case] = 'E' #Ether
                    else:
                        self.struct[i_line][i_case] = ' ' #blank
                    count_S += 1
                i_case += 1
            i_line += 1
        
        print(self.struct)


    def what(self, position):
        """ Return what is at position """

        x = position[0]
        y = position[1]

        thing = self.struct[x][y]

        return thing

    def find(self, thing):
        """ Return the position of the differents elements on map """

        pos = [] #current position

        i_line = 0
        for line in self.struct:
            i_case = 0

            for case in line:
                if case == 'M' and thing == 'M': #mac position
                    pos = [i_line, i_case]
                    print("M ", i_line, i_case)
                elif case == 'G' and thing == 'G': #guard position
                    pos = [i_line, i_case]
                    print("G ", i_line, i_case)
                elif case == 'N' and thing == 'N': #nedle position
                    pos = [i_line, i_case]
                    print("N ", i_line, i_case)
                elif case == 'T' and thing == 'T': #tube position
                    pos = [i_line, i_case]
                    print("T ", i_line, i_case)
                elif case == 'E' and thing == 'E': #ether position
                    print("E ", i_line, i_case)
                    pos = [i_line, i_case]
                
                i_case += 1
            i_line += 1
        
        print(pos)
        return (pos)

    def pick(self, item):
        """ Replace the position of an item picked by a blank """

        pos = self.find(item)
        x = pos[0]
        y = pos[1]

        self.struct[x][y] = ' '
