#!/bin/python3
# Coding:Utf-8

import pygame
from time import sleep
from pygame.locals import *

from labyrinth.characters import Character, Hero
from labyrinth.const import *
from labyrinth.items import *
from labyrinth.level import *

class Game():
    """Main object"""

    def __init__(self):
        self.loop = True
        self.Win = pygame.display.set_mode((WIN_SIZE, WIN_SIZE)) #init the window
        self.Level = Level() #init the Level

        ############# Item init #########################
        self.Needle = Items()
        self.Tube = Items()
        self.Ether = Items()

        ############# Characters init ###################
        self.Mac = Hero() #init macgyver
        self.Guard = Character() #init the guard
    

    def init_pos(self):
        """Set the original position for all objects in map"""

        ############# Chars positions ###################

        self.Mac.set_position(self.Level.find('M'))
        print("guard")
        self.Guard.set_position(self.Level.find('G'))
        
        ############# Items positions ###################

        print("needle")
        self.Needle.set_position(self.Level.find('N'))
        print("tube")
        self.Tube.set_position(self.Level.find('T'))
        print("ether")
        self.Ether.set_position(self.Level.find('E'))

    def init_sprite(self):
        """Load the source image for objects from ./ressources"""

        self.Mac.init_sprite(MACGYVER)
        self.Guard.init_sprite(GUARD)
        
        self.Needle.init_sprite(NEEDLE)
        self.Tube.init_sprite(TUBE)
        self.Ether.init_sprite(ETHER)

    def display(self):
        """display on win all elements if they are still available"""
        self.Level.display(self.Win) #display the background and walls
        
        ############# Items display ######################

        if self.Needle.is_available():
            self.Needle.display(self.Win)

        if self.Tube.is_available():
            self.Tube.display(self.Win)

        if self.Ether.is_available():
            self.Ether.display(self.Win)

        ############## Characters display ###############

        if self.Mac.is_alive():
            self.Mac.display(self.Win)

        if self.Guard.is_alive():
            self.Guard.display(self.Win)

    def win_or_loose(self):
        """ Show the ending image if Mac or guard is dead """

        if self.Guard.is_alive() == False:
            game_won = pygame.image.load(GAME_WON).convert()
            self.Win.blit(game_won, (0,0))
            sleep(1) #wait for show to the player he's move
            pygame.display.flip()
            sleep(20)
            self.loop = False

        elif self.Mac.is_alive() == False:
            game_lost = pygame.image.load(GAME_LOST).convert()
            self.Win.blit(game_lost, (0,0))
            sleep(1)
            pygame.display.flip()
            sleep(10)
            self.loop = False

        else:
            return 0
        
    def event(self, ev):
        """ Manage the events after a move """

        if ev == 'N' and self.Needle.is_available() == True:
            self.Needle.picked()

        elif ev == 'T' and self.Tube.is_available() == True:
            self.Tube.picked()

        elif ev == 'E' and self.Ether.is_available() == True:
            self.Ether.picked()

        elif ev == 'G':
            if self.Mac.can_kill():
                self.Guard.pawned()
            else:
                self.Mac.pawned()

        else:
            pass
        



    def main(self):
        """Launch the game"""

        ############# Initialisation ##########################

        self.Level.make() #Generate the Level from Level.txt
        self.Level.init_spawn() #Generate spawn in Level structure
        self.init_pos() # Find the original position for all objects
        print("mac pos : ", self.Mac.x, self.Mac.y)
        self.init_sprite() #initialise the png for GUI

        ############# Main loop ###############################

        while self.loop:
            
            ev = '' #caption the event after a move

            pygame.time.Clock().tick(TICKRATE) #set a tick limit for win

            for event in pygame.event.get():
                #Caption the key pressed by user

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.loop = False

                    # QWERTY USER !
                    if event.key == K_w:
                        ev = self.Mac.move(self.Level, 'up')
                    if event.key == K_s:
                        ev = self.Mac.move(self.Level, 'down')
                    if event.key == K_a:
                        ev = self.Mac.move(self.Level, 'left')
                    if event.key == K_d:
                        ev = self.Mac.move(self.Level, 'right')
                    

            print("EV ",ev)
            self.event(ev)
            self.display()
            pygame.display.flip()
            self.win_or_loose()
            

if __name__ == "__main__":
    Game = Game()
    Game.main()