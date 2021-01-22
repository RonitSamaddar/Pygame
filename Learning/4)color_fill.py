##Example game = Snake game

#Here we will be drawing shapes to the screen


import pygame


#Defining the colours

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

pygame.init() 
display=pygame.display.set_mode((800,600))

pygame.display.set_caption("Slither")

pygame.display.update()

gameExit=False
while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True


		display.fill(BLUE)
		pygame.display.update()
		



pygame.quit()
quit()