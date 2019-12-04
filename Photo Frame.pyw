#!/usr/bin/python3
Version = "Photoframe 1.2"
import pygame
import io
import os
import time
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def UpdateScreen(pictureFile):
    screenWidth = pygame.display.Info().current_w
    screenHeight = pygame.display.Info().current_h
    pygame.event.get()
    pygame.mouse.set_visible(0)
            
    screen.fill((0,0,0))
 
    image = pygame.image.load(pictureFile)
    
    imageSize = image.get_rect().size
    ratio = imageSize[0] / imageSize[1]

    if ratio < (screenWidth/screenHeight) -.1:
        #Tall
        width  = int(screenHeight * ratio)
        height = screenHeight
    elif ratio >= (screenWidth/screenHeight) -.1 and ratio <= (screenWidth/screenHeight) +.1:
        #Screen Size
        width  = screenWidth
        height = screenHeight
    else:
        #Wide
        width = screenWidth
        height = int(screenWidth / ratio)
        
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
    directory = "C:/Users/Darren/Desktop/pics/"
    while True:
        picturesInFolder = []
        for file in os.listdir(directory):
            if file.upper().endswith(".JPG") or file.upper().endswith(".PNG") or file.upper().endswith(".TIFF") or file.upper().endswith(".TIF"):
                if os.path.getsize(directory + file)/1000000 < 80:
                    picturesInFolder.append(directory + file)

        random.shuffle(picturesInFolder)
        for picture in picturesInFolder:
            UpdateScreen(picture)
            for i in range(60*3):
                time.sleep(1)
                for event in pygame.event.get(): 
                    if event.type == pygame.KEYDOWN:
                         if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                            pygame.quit()
                            exit()

GetPictures()
