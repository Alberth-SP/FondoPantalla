import random


def get_coords_random():
	return [ random.randint(55,750), random.randint(60,450)]

def get_speed_random(inter_a=1.2, inter_b=1.9):
	sign = random.randint(0,1)
	sign = -1 if sign == 0 else 1
	return round(random.uniform(inter_a, inter_b), 3) * sign

def get_color_random():
	return (		
		random.randint(0,255),
		random.randint(0,255),
		random.randint(0,255),
		)

def get_size_random():
	return 	random.randint(20,60)


