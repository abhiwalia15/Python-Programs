import sys

import pygame

def run_game():
	
	pygame.init
	
	screen = pygame.display.set_mode((800,600))
	pygame.display.set_caption("Print Num")
	background = (230,240,255)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				print(event.key)
		
		screen.fill(background)
		
		pygame.display.flip()
		
run_game()
