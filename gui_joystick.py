import sys
import math
import pygame
import time
from pygame import *
from pygame.locals import *

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

def initializeController():
    pygame.joystick.init()
    names = [pygame.joystick.Joystick(x).get_name() for x in range(pygame.joystick.get_count())]
    print("Choose a device:")
    for i in range(0,pygame.joystick.get_count()):
        print(i,": ", names[i])
    deviceNum = int(input("> "))
    controller = pygame.joystick.Joystick(deviceNum)
    controller.init()
    return controller

def initializeDisplay():
    displayWidth = 900
    displayHeight = 400
    icon = pygame.image.load("jrti.png")
    display = pygame.display.set_mode((displayWidth,displayHeight),0,10)
    pygame.display.set_caption('GUI Joystick Tester')
    pygame.display.set_icon(icon)
    return display

def drawXInput(window, controller):
    pygame.event.pump()
    width = 4
    height = (0 - (100 * controller.get_axis(1)))
    xPosition = (pygame.display.get_window_size()[0]/2) - (width/2)
    yPosition = 0
    if height >= 0:
        yPosition = 200 - height
    else:
        yPosition = 200
    pygame.draw.rect(window,blue,(xPosition, yPosition, width, abs(height)))

def drawYInput(window, controller):
    pygame.event.pump()
    width = (0 - (100 * controller.get_axis(0)))
    height = 4
    xPosition = 0
    yPosition = (pygame.display.get_window_size()[1]/2) - (height/2)
    if width >= 0:
        xPosition = 450 - width
    else:
        xPosition = 450
    pygame.draw.rect(window,blue,(xPosition, yPosition, abs(width), height))

def drawAxisBox(window):
    # Draw a rectangle outline
    pygame.draw.rect(window, black, [350, 100, 200, 200], 2)
    pygame.draw.line(window, black, (350, 199), (550,199), 2)
    pygame.draw.line(window, black, (449, 100), (449, 300), 2)
def main():
    pygame.init()

    controller = initializeController()
    window = initializeDisplay()
    
    while True:
        window.fill(white)
        pygame.draw.rect(window,blue,(448, 198, 4, 4))
        pygame.draw.line(window, green, (449,199), (449+(100 * controller.get_axis(0)), 199+(100 * controller.get_axis(1))), 2)
        pygame.draw.rect(window,red,(448 + (100 * controller.get_axis(0)), 198 + (100 * controller.get_axis(1)), 4, 4))
        pygame.draw.line(window, green, (449,199), (449+(100 * controller.get_axis(0)), 199+(100 * controller.get_axis(1))), 2)
        drawAxisBox(window)
        drawXInput(window, controller)
        drawYInput(window, controller)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()