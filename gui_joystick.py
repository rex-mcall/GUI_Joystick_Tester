import sys
import math
import pygame
import time
from pygame import *
from pygame.locals import *

# color tuples
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# controller mapping
fwdBack = 1
leftRight = 0
rotate = 4

#display reference
centerX = 1920 / 2
centerY = 1080 / 2
lineWidth = 2
scale = 400
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

def setControllerMap():
    deviceType = int(input("Choose device type:\n0: XBox\n1: Flight Sim Stick\n> "))
    if deviceType == 0:
        pass
    elif deviceType == 1:
        pass
def initializeDisplay():
    displayWidth = 1920
    centerX = displayWidth / 2
    displayHeight = 1080
    centerY = displayHeight / 2
    icon = pygame.image.load("jrti.png")
    display = pygame.display.set_mode((displayWidth,displayHeight),0,10)
    pygame.display.set_caption('GUI Joystick Tester')
    pygame.display.set_icon(icon)
    return display

def drawXInput(window, controller):
    pygame.event.pump()
    width = lineWidth * 2
    height = (0 - (scale * controller.get_axis(fwdBack)))
    xPosition = centerX - (width/2)
    yPosition = 0
    if height >= 0:
        yPosition = centerY - height
    else:
        yPosition = centerY
    pygame.draw.rect(window,red,(xPosition, yPosition, width, abs(height)))

def drawYInput(window, controller):
    pygame.event.pump()
    width = (0 - (scale * controller.get_axis(leftRight)))
    height = lineWidth * 2
    xPosition = 0
    yPosition = centerY - (height/2)
    if width >= 0:
        xPosition = centerX - width
    else:
        xPosition = centerX
    pygame.draw.rect(window,red,(xPosition, yPosition, abs(width), height))

def drawAxisBox(window):
    # Draw a rectangle outline
    pygame.draw.rect(window, white, [centerX - scale, centerY - scale, 2 * scale, 2 * scale], lineWidth)
    pygame.draw.line(window, white, (centerX - scale, centerY), (centerX + scale,centerY), lineWidth)
    pygame.draw.line(window, white, (centerX, centerY - scale), (centerX, centerY + scale), lineWidth)

def main():
    pygame.init()

    controller = initializeController()
    window = initializeDisplay()
    
    while True:
        window.fill(black)
        pygame.draw.rect(window,blue,(centerX, centerY, lineWidth, lineWidth))
        drawAxisBox(window)
        drawXInput(window, controller)
        drawYInput(window, controller)
        pygame.draw.line(window, green, (centerX,centerY), (centerX+(scale * controller.get_axis(leftRight)), centerY+(scale * controller.get_axis(fwdBack))), lineWidth)
        pygame.draw.rect(window,red,(centerX + (scale * controller.get_axis(leftRight)), centerY + (scale * controller.get_axis(fwdBack)), 5, 5)) #final position dot
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()