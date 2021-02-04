##Example game = Snake game

#Here we will be moving rectangles once per arrow key press


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


#Starting coordinates
lead_x=200
lead_y=200

gameExit=False
while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				lead_x-=10
			if event.key==pygame.K_RIGHT:
				lead_x+=10
			if event.key==pygame.K_UP:
				lead_y-=10
			if event.key==pygame.K_DOWN:
				lead_y+=10


		display.fill(BLUE)

		
		pygame.draw.rect(display,RED,[lead_x,lead_y,50,50])
		pygame.display.update()
		



pygame.quit()
quit()