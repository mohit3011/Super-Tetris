import os, sys, math, random;
from random import randint
import pygame
import block
import time

from block import *
from board import *

class Gameplay():

	def __init__(self,dif):
		self.width = 32
		self.height = 30
		self.__fps = 3
		self.__score = 0
		self.__level = 0

	
		self.matrix = [[0 for x in range(0,self.width)] for y in range(0,self.height)]

		if dif!=0:

			self.__fps = 5
			for y in range(4,9):
				self.matrix[12][y] = 3
			for y in range(23,28):
				self.matrix[12][y] = 3

			for x in range(20,22):
				for y in range(15,18):
					self.matrix[x][y] = 4		


	def checkRowFull(self):
		lis = []
		for x in range(0,self.height):
			flag = 0
			for y in range(0,self.width):
				if self.matrix[x][y]==0:
					flag = 1					#For Checking Which rows are full so as to remove them
					y = self.width
			if flag==0:		
				lis.append(x)

		return lis


	def printblock(self,num):
		shape = [  [[0,14],[0,15],[0,16],[0,17]]  ,  [[0,14],[0,15],[1,14],[1,15]]  ,   [[0,15],[1,14],[1,15],[1,16]]  ,  [[0,14],[0,15],[0,16],[1,16]]  ,  [[0,14],[0,15],[1,15],[1,16]]  ,  [[0,15],[0,16],[1,14],[1,15]] ]

		co = shape[num]

		for x in co:
			x[0] += 15							# For Printing the current block on the sidebar
			x[1] += 24
			pygame.draw.rect(gamedisplay,colo[num],[x[1]*20,x[0]*20,19,19])

	def Displayclk(self):
		return self.__fps						# For Using fps in the game loop since it is a private variable

	def checkRowEmpty(self):
		lis = []
		for x in range(0,self.height):
			flag = 0							# for checking ending of the game
			for y in range(0,self.width):
				if self.matrix[x][y]!=0:
					flag = 1
					y = self.width
			if flag==0:		
				lis.append(x)

		return lis

	def levelinc(self):
		self.__level += 1						# increasing the level and fps
		self.__fps += 1
	
	def Displaylevel(self):
		return self.__level						# using the fps in game loop

	def updateScore(self,sco):
		self.__score += sco          			#  updating the score since it is a private variable

	def DisplayScore(self):
	
		return self.__score 					# using the score in game loop to show

	def selectPiece(self):
		shape = [  [[0,14],[0,15],[0,16],[0,17]]  ,  [[0,14],[0,15],[1,14],[1,15]]  ,   [[0,15],[1,14],[1,15],[1,16]]  ,  [[0,14],[0,15],[0,16],[1,16]]  ,  [[0,14],[0,15],[1,15],[1,16]]  ,  [[0,15],[0,16],[1,14],[1,15]] ]
		num = random.randint(0,5)

		for x in shape[num]:
			count = 0
			for y in range(0,len(x)):
				if y==0:
					y1 = x[0]
				else:
					x1 = x[1]
												#for randomly selecting the next piece
			self.matrix[y1][x1] = 1

		return num

	def printboard(self,sco,lev):

		gamedisplay.fill(black)
		for x in range(0,self.height):
			for y in range(0,self.width):
				if self.matrix[x][y]==0:
					pygame.draw.rect(gamedisplay,white,[y*20,x*20,20,20])
				

				elif self.matrix[x][y]==1:
					pygame.draw.rect(gamedisplay,colo[num],[y*20,x*20,19,19])

				elif self.matrix[x][y]==2:
					pygame.draw.rect(gamedisplay,red,[y*20,x*20,19,19])

				elif self.matrix[x][y]==3:												# Printing the whole board
					pygame.draw.rect(gamedisplay,colo[1],[y*20,x*20,19,19])

				elif self.matrix[x][y]==4:
					pygame.draw.rect(gamedisplay,colo[2],[y*20,x*20,19,19])

				elif self.matrix[x][y]==5:
					pygame.draw.rect(gamedisplay,colo[3],[y*20,x*20,19,19])

				elif self.matrix[x][y]==6:
					pygame.draw.rect(gamedisplay,colo[4],[y*20,x*20,19,19])

				elif self.matrix[x][y]==7:
					pygame.draw.rect(gamedisplay,colo[5],[y*20,x*20,19,19])


		font = pygame.font.SysFont("Arial",25,True)
		textSurf = font.render("Score: "+str(score),True,white)
		textRect = textSurf.get_rect()
		textRect.center = (800,50)
		gamedisplay.blit(textSurf,textRect)

		textSurf = font.render("Level: "+str(lev),True,white)
		textRect = textSurf.get_rect()
		textRect.center = (800,200)
		gamedisplay.blit(textSurf,textRect)

		self.printblock(num)


		pygame.display.update()
		clock.tick(fps)




x = pygame.init()
pygame.key.set_repeat(250,25)
gamedisplay = pygame.display.set_mode((940,640)) 			#extra 300 space in the width for the scoreboard thing
pygame.display.set_caption('SuperTetris')


colo = []
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
colo.append(red)
cyan = (0,255,255)										# colors in colo array
colo.append(cyan)
orange = (255,153,51)
colo.append(orange)
pink = (255,51,153)
colo.append(pink)
violet = (153,153,255)
colo.append(violet)
green = (153,255,51)
colo.append(green)

dif = 0
intro = True
while intro:
	
	font = pygame.font.SysFont("Arial",50,True)
	textSurf = font.render("SUPER TETRIS",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (470,220)
	bg = pygame.image.load("back.jpeg")
	bg = pygame.transform.scale(bg, (940, 640))
	bg_top = 0
	bg_left = 0
	gamedisplay.blit(bg, (bg_left,bg_top))

	gamedisplay.blit(textSurf,textRect)
																# welcome page where the user selects the hardness level
	font1= pygame.font.SysFont("Arial",30,True)
	textSurf = font1.render("EASY",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (330,320)
	gamedisplay.blit(textSurf,textRect)

	font1= pygame.font.SysFont("Arial",30,True)
	textSurf = font1.render("HARD",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (600,320)
	gamedisplay.blit(textSurf,textRect)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print x,y
			if x<500 and y>300:									# use mouse to select the level of difficulty
				intro = False
			elif x>500 and y>300:
				intro = False
				dif = 1

gamedisplay.fill(black)

board = Gameplay(dif)


gameexit = False
clock = pygame.time.Clock()						# clock
count = 0
low = 0
rot = -1
fl1 = 0
num = -1
flrot = 0
flspa = 0
templis =[]
nexpie = []
lev = 0
first = 0
qui = 0
end = True

print num
while not gameexit:						# gameloop starts

	fl1 = 0
	flrot = 0
	flspa = 0
	
	if count==1:
		

		if (piece.final[0]+1 !=30) and (piece.final[1]+1 !=30)  and (piece.final[2]+1 !=30) and (piece.final[3]+1!=30) and (board.matrix[piece.final[3]+1][piece.final[7]]< 2) and (board.matrix[piece.final[2]+1][piece.final[6]]< 2) and (board.matrix[piece.final[1]+1][piece.final[5]]< 2) and (board.matrix[piece.final[0]+1][piece.final[4]]< 2):
				

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameexit = True

				if event.type == pygame.KEYDOWN:
															# Pause feature using p key
				
					if event.key == pygame.K_p:	
						if first ==0:
							first= 1
						
						elif first==1:
							first = 0

				
					if first==1:

							font = pygame.font.SysFont("Arial",50,True)
							textSurf = font.render("Game Paused",True,white)
							textRect = textSurf.get_rect()
							textRect.center = (470,220)
							bg = pygame.image.load("back.jpeg")					# displaying the pause feature
							bg = pygame.transform.scale(bg, (940, 640))
							bg_top = 0
							bg_left = 0
							gamedisplay.blit(bg, (bg_left,bg_top))
							gamedisplay.blit(textSurf,textRect)
							pygame.display.update()

							
						
					elif first==0:		
													# if game not paused
						

						if event.type == pygame.KEYDOWN:

							if event.key == pygame.K_a:
						
								if (piece.final[4]-1 !=-1) and (piece.final[5]-1 !=-1)  and (piece.final[6]-1 !=-1) and (piece.final[7]-1!=-1) and (board.matrix[piece.final[3]][piece.final[7]-1]< 2) and (board.matrix[piece.final[2]][piece.final[6]-1]< 2) and (board.matrix[piece.final[1]][piece.final[5]-1]< 2) and (board.matrix[piece.final[0]][piece.final[4]-1]< 2):
									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 0

									piece.final = piece.moveleft(piece.final[0],piece.final[1],piece.final[2],piece.final[3],piece.final[4],piece.final[5],piece.final[6],piece.final[7],-1)

																																																			# left shift									

									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 1

							elif event.key == pygame.K_d:
							
								if (piece.final[4]+1 !=32) and (piece.final[5]+1!=32)  and (piece.final[6]+1!=32) and (piece.final[7]+1!=32) and (board.matrix[piece.final[3]][piece.final[7]+1]< 2) and (board.matrix[piece.final[2]][piece.final[6]+1]< 2) and (board.matrix[piece.final[1]][piece.final[5]+1]< 2) and (board.matrix[piece.final[0]][piece.final[4]+1]< 2):
									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 0

									piece.final = piece.moveright(piece.final[0],piece.final[1],piece.final[2],piece.final[3],piece.final[4],piece.final[5],piece.final[6],piece.final[7],1)

																																																						#right shift

									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 1


							elif event.key == pygame.K_SPACE:
								while flspa!=1:
									if (piece.final[0]+1 !=30) and (piece.final[1]+1 !=30)  and (piece.final[2]+1 !=30) and (piece.final[3]+1!=30) and (board.matrix[piece.final[3]+1][piece.final[7]]<2) and (board.matrix[piece.final[2]+1][piece.final[6]]<2) and (board.matrix[piece.final[1]+1][piece.final[5]]<2) and (board.matrix[piece.final[0]+1][piece.final[4]]<2):

										for i in range(0,4):
											board.matrix[piece.final[i]][piece.final[i+4]] = 0

										piece.final[0] += 1
										piece.final[1] += 1
										piece.final[2] += 1
										piece.final[3] += 1

																																																						#drop the piece
										for i in range(0,4):
											board.matrix[piece.final[i]][piece.final[i+4]] = 1

									else:
										flspa = 1



							elif event.key == pygame.K_s:
								temp = rot
								templis = piece.checkrotate(piece.final[0],piece.final[1],piece.final[2],piece.final[3],piece.final[4],piece.final[5],piece.final[6],piece.final[7],num,rot)
								
								for i in range(0,4):
									print templis[i],templis[i+4]
									if board.matrix[templis[i]][templis[i+4]]==2 or templis[i]<0 or templis[i]>31 or templis[i+4]>29:
										
										flrot = 1
										break

								if flrot==0:
									rot += 1

								if rot!=temp:
									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 0

					
									piece.final = piece.rotate(piece.final[0],piece.final[1],piece.final[2],piece.final[3],piece.final[4],piece.final[5],piece.final[6],piece.final[7],num,rot)

									for i in range(0,4):
										board.matrix[piece.final[i]][piece.final[i+4]] = 1

						elif event.type == pygame.KEYUP:

							if event.key == pygame.K_a:
								pass
							
							elif event.key == pygame.K_d:
								pass
							




			if first==0:
				if flspa!=1:
					for i in range(0,4):
						board.matrix[piece.final[i]][piece.final[i+4]] = 0

					piece.final[0] += 1
					piece.final[1] += 1
					piece.final[2] += 1
					piece.final[3] += 1
																															# movig the piece one down

					for i in range(0,4):
						board.matrix[piece.final[i]][piece.final[i+4]] = 1




		else:
			count = 0
			board.updateScore(10)

	elif count==0:
		for x in range(0,board.height):
			for y in range(0,board.width):
				if board.matrix[x][y]==1:
					board.matrix[x][y] = num+2

		

		lis = board.checkRowFull()		
		board.updateScore(len(lis)*100)
		for x in lis:
			for y in range(0,x):
				
				for z in range(0,board.width):
					board.matrix[x-y][z] = board.matrix[x-y-1][z]

		level = board
		lise = board.checkRowEmpty()

		for x in lise:
			if x==0:
				fl1 = 1
				

		if fl1==0:
			gameexit = True

		score = board.DisplayScore()
		if score%200==0:
			board.levelinc()
			fps = board.Displayclk()				# increment the level and fps after every 200 points
			lev = board.Displaylevel()


		num = board.selectPiece()
		
		piece = block(num)

		board.printblock(num)


		rot = -1
		count += 1

	if first==0:
		board.printboard(score,lev)	

while end:
	
	font = pygame.font.SysFont("Arial",50,True)
	textSurf = font.render("YOU LOSE",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (470,220)
	bg = pygame.image.load("back.jpeg")
	bg = pygame.transform.scale(bg, (940, 640))
	bg_top = 0
	bg_left = 0
	gamedisplay.blit(bg, (bg_left,bg_top))

	gamedisplay.blit(textSurf,textRect)
																#quit and restart option
	font1= pygame.font.SysFont("Arial",30,True)
	textSurf = font1.render("QUIT",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (330,320)
	gamedisplay.blit(textSurf,textRect)

	font1= pygame.font.SysFont("Arial",30,True)
	textSurf = font1.render("PLAY AGAIN",True,white)
	textRect = textSurf.get_rect()
	textRect.center = (600,320)
	gamedisplay.blit(textSurf,textRect)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print x,y
			if x<500 and y>300:
				pygame.quit()
				quit()	
			elif x>500 and y>300:
				
				qui = 1
				end = False


	