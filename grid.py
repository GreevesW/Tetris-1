

import pygame
from colors import Colors

class Grid:
	def __init__(self):
		self.num_rows = 20
		self.num_cols = 10
		self.cell_size = 30

		# draws a list of lists of zeros (saves space over writting out the individual lists)
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		self.colors = Colors.get_cell_colors()

	#prints the empty grid row by row (used in testing)
	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ")
			print()

	#Checks if a given tile position is inside the grid
	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

	#checks to see if a block will collide with an existing block that has been locked in place
	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

	#Checks whether a row is full
	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True
		#checks if any of the cells in a row is empty ( =0)

	#If there are no empty cells in a row, this method clears the row
	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

	#moves a row down, if the row/rows below it have been cleared
	#num_rows refers to how many rows the row needs to be moved down
	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

	#combines the previous row functions to check if rows need to be cleared by going through all of them from botom to top
	def clear_full_rows(self):
		completed = 0
		for row in range(self.num_rows-1, 0, -1):
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed

	#A method for resetting the game grid when the game is over
	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0

	#draws the grid during the game
	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column]
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1)
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)

