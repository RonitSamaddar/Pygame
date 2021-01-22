##Example game = Snake game

#Here we will be adding basic game loop and characteristics


import pygame

pygame.init() 
display=pygame.display.set_mode((800,600))

pygame.display.set_caption("Slither")
#Setting the name that is to be displayed in the title bar of the game window


pygame.display.update()

gameExit=False
while not gameExit:
	#This is the basic game loop

	for event in pygame.event.get():
		print(event)
		if event.type==pygame.QUIT:
			gameExit=True
		#Event handling is to be performed here



pygame.quit()
quit()