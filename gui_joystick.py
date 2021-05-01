import sys
import pygame
import time
from pygame import *
from pygame.locals import *

def main():
    pygame.init()

    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    names = [pygame.joystick.Joystick(x).get_name() for x in range(pygame.joystick.get_count())]
    print("Choose a device:")
    for i in range(0,pygame.joystick.get_count()):
        print(i,": ", names[i])
    deviceNum = int(input("> "))
    xbox = pygame.joystick.Joystick(deviceNum)
    xbox.init()

    pygame.init()

    displayWidth = 900
    displayHeight = 400
    display = pygame.display.set_mode((displayWidth,displayHeight),0,10)
    pygame.display.set_caption('GUI Joystick Tester')

    white = (255,255,255)
    blue = (0,0,255)

    while True:
        display.fill(white)
        pygame.event.pump()
        width = 100
        height = 50
        xPosition = ((displayWidth/2) - (width/2)) + (200 * xbox.get_axis(0))
        yPosition = ((displayHeight/2) - (height/2)) + (100 * xbox.get_axis(1))
        pygame.draw.rect(display,blue,(xPosition, yPosition, width, height))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()