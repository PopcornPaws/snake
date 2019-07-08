import numpy as np
import curses
## Class describing our snake
class Snake:
	def __init__(self, head, speed):
		self.__x	= head[0]
		self.__y	= head[1]
		self.__vx	= speed[0] 
		self.__vy	= speed[1] 
		self.__length	= 1
		self.__color	= 1
		self.__shape	= '#'

	def __repr__(self):
		return "Snake with length {:}".format(self.__length)

	def check_if_crashed(self, rows : int, columns : int):
		if self.__x[0] <= 0 or self.__x[0] >= columns - 1:
			return 1
		if self.__y[0] <= 0 or self.__y[0] >= rows - 1:
			return 1
		for i in range(self.__length - 1):
			if self.__x[0] == self.__x[i + 1] and self.__y[0] == self.__y[i + 1]:
				return 1
		# if none is true return 0
		return 0

	def increase_length(self):
		self.__length += 1
		self.__x.append(-1 * np.sign(self.__vx[-1]) + self.__x[-1])
		self.__y.append(-1 * np.sign(self.__vy[-1]) + self.__y[-1])
	
	def move(self, direction : int):
		# direction key codes: UP = -1, DOWN = 1, LEFT = -2, RIGHT = 2
		# turn head up or down 
		if self.__vx != 0 and abs(direction) == 1:
			self.__vy[0] = np.sign(direction) * abs(self.__vx[0])
			self.__vx[0] = 0
			self.__y[0] += self.__vy[0]
		# turn head left or right 
		elif self.__vy != 0 and abs(direction) == 2:
			self.__vx[0] = np.sign(direction) * abs(self.__vy[0])
			self.__vy[0] = 0
			self.__x[0] += self.__vx[0]
		# propagate snake body
		for i in range(self.__length - 1):
			self.__x[i + 1] += self.__vx[i + 1]
			self.__y[i + 1] += self.__vy[i + 1]
			self.__vx[i + 1] = self.__vx[i]
			self.__vy[i + 1] = self.__vy[i]

	def head_pos(self):
		return self.__x[0], self.__y[0]

	def draw(self, window):
		for i in range(self.__length):
			window.addch(self.__y[i], self.__x[i], self.__shape, curses.color_pair(self.__color)) 
		
