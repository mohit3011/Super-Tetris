import os,sys


from gameplay import *

class board(Gameplay):
	def __init__self(self):
		self.width = 32					# board class which inherits the Gameplay class
		self.height = 30	
		




	def checkPiecePos(self,x1,x2,x3,x4,y1,y2,y3,y4):

		if (x1+1 !=30) and (x2+1 !=30)  and (x3+1 !=30) and (x4+1!=30) and (self.matrix[x4+1][y4]!=2) and (self.matrix[x3+1][y3]<2) and (self.matrix[x2+1][y2]<2) and (self.matrix[x1+1][y1]<2):
			
			self.matrix[x1][y1] = 0
			self.matrix[x2][y2] = 0
			self.matrix[x3][y3] = 0
			self.matrix[x4][y4] = 0

			x1 += 1
			x2 += 1											# checks whether the piece can move or not
			x3 += 1
			x4 += 1


			self.matrix[x1][y1] = 1
			self.matrix[x2][y2] = 1
			self.matrix[x3][y3] = 1
			self.matrix[x4][y4] = 1




	def fillPiecePos(self):
		
		for x in range(0,self.height):
			for y in range(0,self.width):
				if self.matrix[x][y]==1:				# permanently fill the position of blocks
					self.matrix[x][y] = 2
