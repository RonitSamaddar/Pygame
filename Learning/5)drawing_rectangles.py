##Example game = Snake game

#Here we will be drawing 


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

		#We can draw a rect as follows
		# pygame.draw.rect(surface to draw on, color, [top left x, top left y, width, height])
		# Coordinates start from 0,0 in the top left
		pygame.draw.rect(display,RED,[475,200,50,300])

		#We can also draw a rectangle using fill
		display.fill(GREEN,rect=[475,200,50,50])
		pygame.display.update()
		



pygame.quit()
quit()