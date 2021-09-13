from figura import *
from other import *
import pygame

class Square(Figura):
	def __init__(self, cor_x, cor_y, size ):
		super().__init__(cor_x, cor_y)
		self.spped_x = get_speed_random()
		self.spped_y = get_speed_random()
		self.color = ()
		self.size = size
		self.name = "SQUARE"

	def get_cor_x(self):
		return self.x

	def get_cor_y(self):
		return self.y

	def revert_speed_x(self):
		self.spped_x *= -1

	def revert_speed_y(self):
		self.spped_y *= -1

	def update_cor_x(self):
		self.x += self.spped_x

	def update_cor_y(self):
		self.y += self.spped_y

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setSize(self, size):
		self.size = size


	def getSize(self):
		return self.size

	def getName(self):
		return self.name

	def draw(self, surface):
		pygame.draw.rect(surface, self.color , (self.x, self.y, self.size, self.size))

	def update(self):
		if (self.x + self.size) > 800 or self.x < 0:
			self.revert_speed_x()
		if (self.y + self.size) > 500 or self.y < 0:
			self.revert_speed_y()
		self.update_cor_x()
		self.update_cor_y()