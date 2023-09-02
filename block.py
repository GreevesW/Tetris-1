
from colors import Colors
import pygame
from position import Position

#parent class for the blocks that can be used to inherit features for subclasses of blocks

class Block:
	def __init__(self, id):
		self.id = id
		# uses the block id to determine its size and shape and colour on screen

		#creating a dictionary
		self.cells = {}

		#sets the position of the block on screen
		self.cell_size = 30
		self.row_offset = 0
		self.column_offset = 0
		self.rotation_state = 0

		#Sets a colour for each block on screen
		self.colors = Colors.get_cell_colors()
	

	#This method logically moves the block ( calcluates new block position)
	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns
		#Applies the offset to the block

	#returns the list of occupied cells as a list (after the ofset has been applied) 
	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]
		moved_tiles = []
		for position in tiles:
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	#rotates the block
	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells):
			self.rotation_state = 0

	#undoes the rotation if the block clips through the edge
	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	#method for drawing the block including the +1 and -1 as borders to keep the grid look
	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions()
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, 
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)
