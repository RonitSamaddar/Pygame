##Example game = Snake game

#Here we will be moving rectangles and setting frames per second


import pygame


WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

pygame.init() 
display=pygame.display.set_mode((800,600))

clock=pygame.time.Clock()
#Clock Object for defining things like frames per second(fps)

pygame.display.set_caption("Slither")

pygame.display.update()


#Starting coordinates
lead_x=200
lead_y=200
x_change=0
y_change=0



gameExit=False
while not gameExit:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			gameExit=True
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-1
				y_change=0
			if event.key==pygame.K_RIGHT:
				x_change=1
				y_change=0
			if event.key==pygame.K_UP:
				y_change=-1
				x_change=0
			if event.key==pygame.K_DOWN:
				y_change=1
				x_change=0

	lead_x+=x_change
	lead_y+=y_change


	display.fill(WHITE)
	pygame.draw.rect(display,BLACK,[lead_x,lead_y,10,10])
	pygame.display.update()

	clock.tick(100)#defining fps
		



pygame.quit()
quit()