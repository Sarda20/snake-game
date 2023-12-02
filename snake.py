import pygame
from pygame.locals import *

def draw_food():
    background.fill((4,41,59))
    background.blit(food,(food_x,food_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    background=pygame.display.set_mode((500,500))
    background.fill((4,41,59))

    food=pygame.image.load("images/food.jpg").convert()
    food_x,food_y=100,100
    
    background.blit(food,(food_x,food_y))
    pygame.display.flip()

    running=True

    while running:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    running=False
                if event.key==K_DOWN:
                    food_y += 10
                    draw_food()
                if event.key==K_UP:
                    food_y -= 10
                    draw_food()
                if event.key==K_RIGHT:
                    food_x += 10
                    draw_food()
                if event.key==K_LEFT:
                    food_x -= 10
                    draw_food()
                
            elif event.type==QUIT:
                running=False