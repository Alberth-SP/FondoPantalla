import pygame, sys
import random
from other import *
from figura import *
from circle import *
from square import *


def get_figure_random():
	op = random.randint(0,1)
	coords = get_coords_random()
	size = get_size_random()
	figure = None
	if op == 1:
		figure = Circle(coords[0], coords[1], size)
	else:
		figure = Square(coords[0], coords[1], size)
	figure.setColor(get_color_random())
	return figure


def rungame():
	pygame.init()
	count = 1	
	screen = pygame.display.set_mode((800, 500))	
	figura = get_figure_random()

	#pygame.mixer.Sound('desc.ogg').play()
	figuras = []
	figuras.append(figura)
	end = False
	clock = pygame.time.Clock()
	screen.fill((244, 239, 247))

	pygame.draw.circle(screen, (0,0,255), (0,0),50)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
		if end:
			break
		screen.fill((244, 239, 247))
		
		count += 1
		if count > 100:
			count = 0
			figura = get_figure_random()
			figuras.append(figura)


		for figura in figuras:
			figura.draw(screen)
			figura.update()


			
		pygame.display.flip()
		clock.tick(60)


rungame()


