import os,sys


class block():

	def __init__(self,num):
		self.shape = [  [[0,14],[0,15],[0,16],[0,17]],   [[0,14],[0,15],[1,14],[1,15]],  [[0,15],[1,14],[1,15],[1,16]],  [[0,14],[0,15],[0,16],[1,16]],  [[0,14],[0,15],[1,15],[1,16]],  [[0,15],[0,16],[1,14],[1,15]] ]
		self.final = []
		self.lis = [   [[[2,2],[1,1],[0,0],[-1,-1]],[[-2,2],[-1,1],[0,0],[1,-1]],[[-2,-2],[-1,-1],[0,0],[1,1]],[[2,-2],[1,-1],[0,0],[-1,1]]],    [[[0,0],[0,0],[0,0],[0,0]]]    ,[[[1,-1],[1,1],[0,0],[-1,-1]],[[1,1],[-1,1],[0,0],[1,-1]],[[-1,1],[-1,-1],[0,0],[1,1]],[[-1,-1],[1,-1],[0,0],[-1,1]]],   [[[1,1],[0,0],[-1,-1],[-2,0]],[[-1,1],[0,0],[1,-1],[0,-2]],[[-1,-1],[0,0],[1,1],[2,0]],[[1,-1],[0,0],[-1,1],[0,2]]],   [[[2,0],[1,-1],[0,0],[-1,-1]],[[0,2],[1,1],[0,0],[1,-1]],[[-2,0],[-1,1],[0,0],[1,1]],[[0,-2],[-1,-1],[0,0],[-1,1]]],   [[[1,-1],[0,-2],[1,1],[0,0]],[[1,1],[2,0],[-1,1],[0,0]],[[-1,1],[0,2],[-1,-1],[0,0]],[[-1,-1],[-2,0],[1,-1],[0,0]]]  ]
		for x in self.shape[num]:
			self.final.append(x[0])
			
		for x in self.shape[num]:
			self.final.append(x[1])					# contains block shapes and possible rotations

		

	
		

	def rotate(self,x1,x2,x3,x4,y1,y2,y3,y4,num,rot):

		listi = self.lis[num]
		length = len(listi)
		new = (rot)%length

		rota = listi[new]
		co = []
		cod = []

		i = 0
		for x in rota:							# rotate the block polymorphism applied

			
			co.append(x[0])
			co.append(x[1])

		cod.append(x1+co[0])
		cod.append(x2+co[2])
		cod.append(x3+co[4])
		cod.append(x4+co[6])
		cod.append(y1+co[1])
		cod.append(y2+co[3])
		cod.append(y3+co[5])
		cod.append(y4+co[7])
		

		
		
		return cod


	def moveleft(self,x1,x2,x3,x4,y1,y2,y3,y4,change):


		co = []
		co.append(x1)
		co.append(x2)
		co.append(x3)
		co.append(x4)
		co.append(y1)
		co.append(y2)
		co.append(y3)
		co.append(y4)

																# move the block left

		if co[4]!=0 and co[5]!=0 and co[6]!=0 and co[7]!=0:

			co[4] = co[4] + change
			co[5] = co[5] + change
			co[6] = co[6] + change
			co[7] = co[7] + change


		return co


	def moveright(self,x1,x2,x3,x4,y1,y2,y3,y4,change):


		co = []
		co.append(x1)
		co.append(x2)
		co.append(x3)
		co.append(x4)
		co.append(y1)
		co.append(y2)
		co.append(y3)
		co.append(y4)

		if co[4]!=31 and co[5]!=31 and co[6]!=31 and co[7]!=31:
																	#move the block right
			co[4] = co[4] + change
			co[5] = co[5] + change
			co[6] = co[6] + change
			co[7] = co[7] + change


		
		return co

	def checkrotate(self,x1,x2,x3,x4,y1,y2,y3,y4,num,rot):
		
		listi = self.lis[num]
		length = len(listi)
		new = (rot+1)%length

		rota = listi[new]
		co = []
		cod =[]

		for x in rota:

			co.append(x[0])
			co.append(x[1])
																# check if rotation is possible

		cod.append(x1+co[0])
		cod.append(x2+co[2])
		cod.append(x3+co[4])
		cod.append(x4+co[6])
		cod.append(y1+co[1])
		cod.append(y2+co[3])
		cod.append(y3+co[5])
		cod.append(y4+co[7])
		

		
		
		return cod