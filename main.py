#! python3
#main file for game

import pygame
from pygame import *
import sys
import random


pygame.init()
screeninfo = pygame.display.Info()
screenSize = (screeninfo.current_w,screeninfo.current_h)
width, height = (screeninfo.current_w, screeninfo.current_h)
clock = pygame.time.Clock()
color = (255,255,255)
screen = pygame.display.set_mode(screenSize)


def main():


    clock.tick(60)

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        
        screen.fill(color)
        pygame.display.flip()

main()

