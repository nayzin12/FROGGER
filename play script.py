
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

def loop(x,limit,reset):
    if limit > 0:
        if x >= limit:
            x = reset
            return x
    if limit < 0:
        if x <= limit:
            x = 616
            return x
    return x
def lane1(car,speed):
    car -= speed
    car = loop(car,-100,616)
    return car

def lane2(car,speed):
    car += speed
    car = loop(car,616,-100)
    return car

def lane3(car,speed,reset):
    car -= speed
    car = loop(car,-120,reset)
    return car

def lane4(car,speed,reset):
    car -= speed
    car = loop(car,-100,reset)
    return car

def main():
    

    pygame.init()
     
    fps = 60
    fpsClock = pygame.time.Clock()
     
    width, height = 516,650
    screen = pygame.display.set_mode((width, height))
    
    x_speed1 = 2
    x_speed2 = 4
    x_speed3 = 6
    
    car1x = 616
    
    car2x = -100
    car3x = -300
    car4x = -500
    
    car5x = 650
    car6x = 820
    car7x = 990
    car8x = 1160
    
    car9x = 700
    car10x = 850
    car11x = 1000
    car12x = 1150
    car13x = 1300

    deltax=0
    deltay=0
    
     
    # Game loop.
    while True:
      screen.fill((0, 0, 0))
      
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()

        if event.type == pygame.KEYDOWN:
                key = event.dict['key']
                if key == pygame.K_UP:
                    deltay-=40
                     
                elif key == pygame.K_LEFT:
                   deltax-=40
                   left=True
                elif key == pygame.K_RIGHT:
                   deltax+=40
                   left=False
                elif key == pygame.K_DOWN:
                    deltay+=40
                else:
                   deltax=0
      
      # Update.
      
      background_image=pygame.image.load("background.png")
    
      spread_sheet=pygame.image.load("frogger.png")

      car_type1=spread_sheet.subsurface(110,47,50,40)

      car_type2=spread_sheet.subsurface(115,203,50,40)

      car_type3=spread_sheet.subsurface(45,128,120,47)

      car_type4=spread_sheet.subsurface(105,270,55,45)

      frog=spread_sheet.subsurface(300,47,50,40)

      carx_list = [car1x,car2x,car3x,car4x,car5x,car6x,car7x,car8x,car9x,car10x,car1x,car12x,car13x]

      
      # Draw.
      #Each lane have 5 pixels between them
      #Each lane is 45 pixels wide
      screen.blit(background_image,[0,0])
      
      #Lane 1 (420)
      car1x = lane1(car1x, x_speed1)
      screen.blit(car_type1,[car1x,420])

      #Lane 2 (375)
      car2x = lane2(car2x,x_speed1)
      car3x = lane2(car3x,x_speed1)
      car4x = lane2(car4x,x_speed1)
      screen.blit(car_type2,[car2x,375])
      screen.blit(car_type2,[car3x,375])
      screen.blit(car_type2,[car4x,375])

      #Lane 3 (323)
      car5x = lane3(car5x,x_speed2,650)
      car6x = lane3(car6x,x_speed2,820)
      car7x = lane3(car7x,x_speed2,990)
      car8x = lane3(car8x,x_speed2,1160)
      screen.blit(car_type3,[car5x,323])
      screen.blit(car_type3,[car6x,323])
      screen.blit(car_type3,[car7x,323])
      screen.blit(car_type3,[car8x,323])

      #Lane 4 (278)
      car9x = lane4(car9x,x_speed3,700)
      car10x = lane4(car10x,x_speed3,850)
      car11x = lane4(car11x,x_speed3,1000)
      car12x = lane4(car12x,x_speed3,1150)
      car13x = lane4(car13x,x_speed3,1300)
      screen.blit(car_type4,[car9x,278])
      screen.blit(car_type4,[car10x,278])
      screen.blit(car_type4,[car11x,278])
      screen.blit(car_type4,[car12x,278])
      screen.blit(car_type4,[car13x,278])

      screen.blit(frog,[258+deltax,590+deltay])

     
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()

