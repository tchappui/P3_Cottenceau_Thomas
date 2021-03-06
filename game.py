#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import random
import pygame
from pygame.locals import *
import maze_structure

""" This file is the execution of the game. """

pygame.init()  # initialisation of all modules in pygame

def main():

    pygame.display.set_caption("__________Mac_Gyver's_Maze__________") # the name of the game
    FPS = 60 # the number of frames per second
    clock = pygame.time.Clock() # creation of a clock to get a fixe speed of updating
    window = pygame.display.set_mode((600, 600)) # creation of the MacGyver game's window
    floor = pygame.image.load("ressource/floor.png").convert() # creation of the background
    window.blit(floor, (0, 0))
    bgd = floor
    song_game = pygame.mixer.music.load("ressource/song.mid") # we put the game song
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)
    i = 0 # to count how many items MacGyver caught

    maze = maze_structure.build_maze()

    class Items(pygame.sprite.Sprite): # we create a class for the items to catch

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)          
            self.image = pygame.image.load("ressource/needle.png").convert()
            self.rect = self.image.get_rect()
            self.rect.center = (0, 0)
            
    def put_items(): # and then we create a methode to put items randomly in the maze

        positions_items = [(60,460),(140,340),(340,540),(540,380),(540,60),(460,180),
        (300,60),(180,220),(300,140)] # we choose the places

        needle = Items()
        needle.image = pygame.image.load("ressource/needle.png").convert()
        random_position = random.choice(positions_items)
        needle.rect.center = random_position  # we attribute randomly the place from position_items
        positions_items.remove(random_position) # to avoid that two items get the same place

        tube = Items()
        tube.image = pygame.image.load("ressource/tube.png").convert()
        random_position = random.choice(positions_items)
        tube.rect.center = random_position
        positions_items.remove(random_position)
        
        ether = Items()
        ether.image = pygame.image.load("ressource/ether.png").convert()
        random_position = random.choice(positions_items)
        ether.rect.center = random_position

        group_items.add(needle) # we put all items in the group made for, and update it to draw
        group_items.add(tube)
        group_items.add(ether)
        group_items.update() 
        group_items.draw(window)
              
        return group_items

    group_items = pygame.sprite.Group()
    put_items()
    

    class Gard(pygame.sprite.Sprite): # we create a class only fo the gard

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("ressource/gard.png").convert()
            self.rect = self.image.get_rect()
            self.rect.center = (580, 300)

    gard = Gard() # we put the gard in his group and update and draw him.
    group_gard = pygame.sprite.Group()
    group_gard.add(gard)
    group_gard.update()
    group_gard.draw(window)
    pygame.display.flip()


    class MacGyver(pygame.sprite.Sprite): # finally we create the player MacGyver in the same way.

        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load("ressource/macgyver.png").convert()
            self.rect = self.image.get_rect()
            self.rect.center = (20, 300)

        def up(self): # the moves of MacGver are mades by four methodes from his class.
            self.rect.y -= 40

        def right(self):
            self.rect.x += 40

        def down(self):
            self.rect.y += 40

        def left(self):
            self.rect.x -= 40

    player = MacGyver() # we put MacGyver in his group, update and drawn him.
    group_player = pygame.sprite.Group()
    group_player.add(player)
    group_player.update()
    group_player.draw(window)
    pygame.display.flip()

    game_on = True

    while game_on: # creation of a loop to maintain the window open

        if i == 0:
            count0 = pygame.image.load("ressource/i=0.png").convert()
            window.blit(count0, (560, 0))        
        elif i == 1:
            count1 = pygame.image.load("ressource/i=1.png").convert()
            window.blit(count1, (560, 0))
        elif i == 2:
            count2 = pygame.image.load("ressource/i=2.png").convert()
            window.blit(count2, (560, 0))
        elif i == 3:
            count3 = pygame.image.load("ressource/i=3.png").convert()
            window.blit(count3, (560, 0))

        for event in pygame.event.get():

            if event.type == QUIT: # if the gamer want to quit the game he clic the cross 
                game_on = False    # on the rifgt top of the window

            elif pygame.sprite.spritecollide(player, group_items, True):
                i += 1

            elif event.type == KEYDOWN and event.key == K_UP:
                player.up()
                if pygame.sprite.spritecollide(player, maze, True):
                    player.down()
                    maze = maze_structure.build_maze()

                else:
                    group_player.clear(window, bgd)
                    group_player.draw(window)
                    pygame.display.flip()

            elif event.type == KEYDOWN and event.key == K_RIGHT:
                player.right()

                if pygame.sprite.spritecollide(player, maze, True):
                    player.left()
                    maze = maze_structure.build_maze()

                elif pygame.sprite.spritecollide(player, group_gard, True):

                    if i == 3:
                        win = pygame.image.load("ressource/win.png").convert()
                        group_gard.empty()
                        group_gard.update()
                        group_gard.draw(window)
                        group_player.empty()
                        group_player.update()
                        group_player.draw(window)
                        pygame.display.flip()
                        pygame.mixer.music.stop()

                        song_win = pygame.mixer.music.load("ressource/win_song.mid")
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.2) # volume
                        window.blit(win, (0, 0))

                    else :
                        game_over = pygame.image.load("ressource/lose.png").convert()
                        group_gard.empty()
                        group_gard.update()
                        group_gard.draw(window)
                        group_player.empty()
                        group_player.update()
                        group_player.draw(window)
                        pygame.display.flip()
                        pygame.mixer.music.stop()
                        
                        song_game_over = pygame.mixer.music.load("ressource/game_over.mid")
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.3) # volume
                        window.blit(game_over, (0, 0))

                else:                    
                    group_player.clear(window, bgd)
                    group_player.draw(window)
                    pygame.display.flip()
                
            elif event.type == KEYDOWN and event.key == K_DOWN:
                player.down()

                if pygame.sprite.spritecollide(player, maze, True):
                    player.up()
                    maze = maze_structure.build_maze()

                else:
                    group_player.clear(window, bgd)
                    group_player.draw(window)
                    pygame.display.flip()
            
            elif event.type == KEYDOWN and event.key == K_LEFT:
                player.left()

                if pygame.sprite.spritecollide(player, maze, True):
                    player.right()
                    maze = maze_structure.build_maze()

                else:
                    group_player.clear(window, bgd)
                    group_player.draw(window)
                    pygame.display.flip()

if __name__ == "__main__":

    main()