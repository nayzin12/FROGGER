

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

def water1(item,speed):
    item -= speed
    item = loop(item,-300,300)
    return item

def water2(item,speed):
    item += speed
    item = loop(item,616,-200)
    return item

def water3(item,speed):
    item -= speed
    item = loop(item,-300,300)
    return item

def main():
    

    pygame.init()
     
    fps = 30
    fpsClock = pygame.time.Clock()
     
    width, height = 516,650
    screen = pygame.display.set_mode((width, height))
    
    x_speed1 = 2
    x_speed2 = 4
    x_speed3 = 6
    
    car1x = 616
    car14x = 816
    car15x = 1016
    
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

    log1x = 650
    log2x = 1100

    log3x = -300
    log4x = -750

    log5x = 650
    log6x = 1100

    lane1y = 420
    lane2y = 375
    lane3y = 323
    lane4y = 278
    water1y = 188
    water2y = 135
    water3y = 75

    car_type1_w = 50
    car_type1_h = 40

    car_type2_w = 50
    car_type2_h = 40

    car_type3_w = 120
    car_type3_h = 47

    car_type4_w = 55
    car_type4_h = 45

    log_type1_w = 223
    log_type1_h = 51

    log_type2_w = 175
    log_type2_h = 57

    deltax=0
    deltay=0


    # Update.
      
    background_image=pygame.image.load("background.png").convert_alpha()
    
    spread_sheet=pygame.image.load("frogger.png").convert_alpha()

    car_type1=spread_sheet.subsurface(110,47,50,40)

    car_type2=spread_sheet.subsurface(115,203,50,40)

    car_type3=spread_sheet.subsurface(45,128,120,47)

    car_type4=spread_sheet.subsurface(105,270,55,45)

    log_type1=spread_sheet.subsurface(277,341,223,51)

    log_type2=spread_sheet.subsurface(275,268,175,57)

    frog=spread_sheet.subsurface(300,47,50,40)
    
     
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
      

      car_list = []
      log_list = []
      carx_list = [car1x,car2x,car3x,car4x,car5x,car6x,car7x,car8x,car9x,car10x,car1x,car12x,car13x,car14x,car15x]
      laney_list = [lane1y,lane2y,lane3y,lane4y]
      logx_list = [log1x,log2x,log3x,log4x,log5x,log6x]
      logy_list = [water1y,water2y,water3y]
      for i in laney_list:
        for q in carx_list:
            car = [q,i]
            car_list.append(car)
      for i in logy_list:
        for q in logx_list:
            log = [q,i]
            log_list.append(log)

      # Draw.
      #Each lane have 5 pixels between them
      #Each lane is 45 pixels wide
      screen.blit(background_image,[0,0])
      
      #Lane 1 (420)
      car1x = lane1(car1x, x_speed1)
      car14x = lane1(car14x, x_speed1)
      car15x = lane1(car15x, x_speed1)
      screen.blit(car_type1,[car1x,lane1y])
      screen.blit(car_type1,[car14x,lane1y])
      screen.blit(car_type1,[car15x,lane1y])

      #Lane 2 (375)
      car2x = lane2(car2x,x_speed1)
      car3x = lane2(car3x,x_speed1)
      car4x = lane2(car4x,x_speed1)
      screen.blit(car_type2,[car2x,lane2y])
      screen.blit(car_type2,[car3x,lane2y])
      screen.blit(car_type2,[car4x,lane2y])

      #Lane 3 (323)
      car5x = lane3(car5x,x_speed2,650)
      car6x = lane3(car6x,x_speed2,820)
      car7x = lane3(car7x,x_speed2,990)
      car8x = lane3(car8x,x_speed2,1160)
      screen.blit(car_type3,[car5x,lane3y])
      screen.blit(car_type3,[car6x,lane3y])
      screen.blit(car_type3,[car7x,lane3y])
      screen.blit(car_type3,[car8x,lane3y])

      #Lane 4 (278)
      car9x = lane4(car9x,x_speed3,700)
      car10x = lane4(car10x,x_speed3,850)
      car11x = lane4(car11x,x_speed3,1000)
      car12x = lane4(car12x,x_speed3,1150)
      car13x = lane4(car13x,x_speed3,1300)
      screen.blit(car_type4,[car9x,lane4y])
      screen.blit(car_type4,[car10x,lane4y])
      screen.blit(car_type4,[car11x,lane4y])
      screen.blit(car_type4,[car12x,lane4y])
      screen.blit(car_type4,[car13x,lane4y])

      #Water 1 (188)
      log1x = water1(log1x,x_speed1)
      log2x = water1(log2x,x_speed1)
      screen.blit(log_type1,[log1x,water1y])
      screen.blit(log_type1,[log2x,water1y])

      #Water 2 (135)
      log3x = water2(log3x,x_speed2)
      log4x = water2(log4x,x_speed2)
      screen.blit(log_type2,[log3x,water2y])
      screen.blit(log_type2,[log4x,water2y])

      #Water 3 (75)
      log5x = water3(log5x,x_speed1)
      log6x = water3(log6x,x_speed1)
      screen.blit(log_type2,[log5x,water3y])
      screen.blit(log_type2,[log6x,water3y])

      screen.blit(frog,[258+deltax,590+deltay])

     
      
      pygame.display.flip()
      fpsClock.tick(fps)

main()

