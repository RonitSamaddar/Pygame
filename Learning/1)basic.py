import pygame

pygame.init() 
#Initializing an instance of pygame

display=pygame.display.set_mode((800,600))
#Getting the background/display surface for the game where all the action will take place

pygame.display.update()
#Updates the display with all the changes that were made before this

pygame.quit()#Quiting or Un-initializing the instance of pygame

quit()#Quiting python