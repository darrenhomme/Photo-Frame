#!/usr/bin/env python3
Version = "Photoframe 1.5"
import pygame
import io
import os
import time
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(0)

def UpdateScreen(pictureFile):
    try:
        imageTest = open(pictureFile)
    except IOError:
        GetPictures()
    finally:
        imageTest.close()

    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h
    pygame.event.get()

    screen.fill((0,0,0))

    image = pygame.image.load(pictureFile)

    imageSize = image.get_rect().size
    ratio = float(imageSize[0]) / float(imageSize[1])

    if (ratio < ((float(screenWidth)/float(screenHeight)) -.1)):
        #Tall
        width  = int(float(screenHeight) * (float(imageSize[0]) / float(imageSize[1])))
        height = screenHeight
    elif (ratio >= ((float(screenWidth)/float(screenHeight)) -.1)) and (ratio <= ((float(screenWidth)/float(screenHeight)) +.1)):
        #Screen Size
        width  = screenWidth
        height = screenHeight
    else:
        #Wide
        width = screenWidth
        height = int(float(screenWidth) * (float(imageSize[1]) / float(imageSize[0])))

    image = pygame.transform.smoothscale(image, (width, height))

    bgImage = image
    bgImage = pygame.transform.smoothscale(bgImage, (screenWidth * 2, screenHeight * 2))
    bgImage.set_alpha(20)
    screen.blit(bgImage, (int(-screenWidth/2), int(-screenHeight/2)))

    offsetWidth = int((screenWidth - width)/2)
    offsetHeight = int((screenHeight - height)/2)
    screen.blit(image, (offsetWidth, offsetHeight))

    pygame.display.update()

def GetPictures():
    directory = "/home/pi/Pictures/"
    while True:
        picturesInFolder = []
        for file in os.listdir(directory):
            if file.upper().endswith(".JPG") or file.upper().endswith(".PNG") or file.upper().endswith(".TIFF") or file.upper().endswith(".TIF"):
                if os.path.getsize(directory + file)/1000000 < 80:
                    picturesInFolder.append(directory + file)

        random.shuffle(picturesInFolder)
        breakSleepLoop = False
        for picture in picturesInFolder:
            UpdateScreen(picture)
            for i in range(8*60*3):
                if breakSleepLoop == True:
                    breakSleepLoop = False
                    break
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        breakSleepLoop = True
                exitFile = open("/home/pi/UpdatePhotoFrame.txt", "r")
                exitFileTxt = str(exitFile.read())
                if exitFileTxt.find("exit") > -1:
                   exitFile = open("/home/pi/UpdatePhotoFrame.txt", "w")
                   exitFile.write("")
                   exitFile.close()
                   exit()
                elif exitFileTxt.find(directory) > -1:
                    exitFile = open("/home/pi/UpdatePhotoFrame.txt", "w")
                    exitFile.write("")
                    exitFile.close()
                    UpdateScreen(exitFileTxt)
                time.sleep(0.125)

GetPictures()
