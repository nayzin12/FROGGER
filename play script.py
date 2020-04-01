#
#
#        Frogger
#
#
#
#################################

import sys
 
import pygame
from pygame.locals import *
     
def main():

    pygame.init()
     
    fps = 60
    fpsClock = pygame.time.Clock()
     
    width, height = 516,680
    screen = pygame.display.set_mode((width, height))
    
    xpos=0
     
    # Game loop.
    while True:
      screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      
      # Update.
      
      background_image=pygame.image.load("background.png")
    
      spread_sheet=pygame.image.load("frogger.png")

      car1=spread_sheet.subsurface((110,47,50,40))

      frog=spread_sheet.subsurface((300,47,50,40))
      
      # Draw.

      screen.blit(background_image,[0,0])
      screen.blit(car1,[(816-xpos)%816-150,425])
      xpos+=3

      screen.blit(frog,[258,590])
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()
