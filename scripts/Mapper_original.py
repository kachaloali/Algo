class DynamicMatrix():
	""" store a matrix  |S| * |T| ( |S| + 1 and |T|+ 1 columns ) ,sequence defines some global alignment functions"""
	def __init__(self, S, T, match, mismatch, gap):
		""" defines and stores initial values """
		self.S = S
		self.T = T
		self.lS = len(S)
		self.lT = len(T)
		self.match = match
		self.mismatch = mismatch
		self.gap = gap
		self.matrix = [[0 for j in range(len(T) + 1)] for i in range(len(S) + 1)]
		self.backtrack = [[(0, 0) for j in range(len(T) + 1)] for i in range(len(S) + 1)]
		
		self.initSemiGlobal()
		self.printSemiGlobalAlin()
 
	def printMatrix(self, width = 5):
		"""Prints the matrix with columns of siez sep """

		#Prof
		line = "{:{w}}".format(" ",w = 2*width)
		for j in range(self.lT):
			line += "{:{w}}".format(self.T[j], w = width)
		print(line)
		line="{:{w}}".format(" ", w = width)
		for j in range(self.lT + 1):
			line+= "{:{w}}".format(str(self.matrix[0][j]), w = width)
		print(line)
		for i in range(1, self.lS + 1):
			line = "{:{w}}".format(self.S[i-1], w = width)
			for j in range(self.lT + 1):
				line+= "{:{w}}".format(str(self.matrix[i][j]), w = width)
			print(line) 


		# Ali

		# print("\t\t"+"\t".join([i for i in self.S]))
		# print("\t"+"\t".join([str(i) for i in self.matrix[0]]))


		# for j in range(1, len(self.matrix)):
		# 	print (self.T[j-1]+"\t" + "\t".join([str(i) for i in self.matrix[j]]))

	def score(self, s, t):
		if s == t:
			return self.match
		return self.mismatch

	def initGlobal(self):
		#self.matrix[0] = [self.gap * i for i in range(1,len(self.S)+1)]
		for i in range(1, self.lS + 1):
			self.matrix[i][0] = self.gap * i
		for j in range(1, self.lT + 1):
			self.matrix[0][j] = self.gap * j
		# self.matrix[0] = [self.gap * i for i in range(1,len(self.S)+1)]
		# for i in range(1, len(self.S)+1):
		# 	self.matrix[0][i] = self.gap * i
		# 	print(self.matrix[0][i])
		# for i in range(0,len(self.T)):
		# 	self.matrix[i][0] = self.gap*i

	def fillGlobal(self):
		for i in range(1, self.lS + 1):
			for j in range(1, self.lT + 1):
				#print(i,j)
				score = max ( 
								(self.matrix[i-1][j-1] + self.score(self.S[i-1], self.T[j-1])),
								(self.matrix[i-1][j] + self.gap),
								(self.matrix[i][j-1] + self.gap)
							)

				self.matrix[i][j] = score

				if score == self.matrix[i-1][j-1] + self.score(self.S[i-1], self.T[j-1]):
					self.backtrack[i][j] = (i-1, j-1)

				elif score == self.matrix[i-1][j] + self.gap:
					self.backtrack[i][j] = (i-1, j)

				else:
					self.backtrack[i][j] = (i, j-1)

	def printGlobalAlin(self):

		Saligne = ""
		Taligne = ""
		(i,j) = (self.lS, self.lT)
		while (i, j) != (0,0):
			(fi, fj) = self.backtrack[i][j]
			if (fi, fj) == (i - 1, j - 1) : 

				Taligne = self.T[j-1] + Taligne 
				Saligne = self.S[i-1] + Saligne 
			elif fi == i : 
				Taligne = self.T[fj:j] + Taligne
				Saligne = "-" * (j - fj) + Saligne

			elif fj == j: 
				Taligne = "-" * (i - fi) + Taligne
				Saligne = self.S[fi:i] + Saligne

			i = fi
			j = fj

		# while (i,j) != (0,0):
		# 	#print (i,j)
		# 	(fi,fj) = self.backtrack[i][j]
		# 	#print(self.matrix[i][j])
		# 	print(i,j)
		# 	if (fi,fj) == (i-1,j-1):
		# 		seqS_alignee = self.S[i-1]+ seqS_alignee
		# 		seqT_alignee = self.T[j-1]+ seqT_alignee
		# 	elif fj == j:
		# 		seqS_alignee = self.S[i-1]+ seqS_alignee
		# 		seqT_alignee = '-'*(j-fj)+ seqT_alignee
		# 	else:
		# 		seqS_alignee = '-'*(i-fi)+ seqS_alignee
		# 		seqT_alignee = self.T[j-1]+ seqT_alignee
		# 	(i,j)=(fi,fj)
		print(Taligne)
		print(Saligne)

	def initSemiGlobal(self):
		for i in range(1, self.lS+1):
			self.matrix[i][0] = self.gap * i
			
		for j in range(1, self.lT + 1):
			self.matrix[0][j] = 0

	def fillSemiGlobal(self):
		self.fillGlobal()
		# for i in range(1, self.lS+1):
		# 		for j in range(1, self.lT+1):
		# 			#print(i,j)
		# 			score = max ( 
		# 							(self.matrix[i-1][j-1] + self.score(self.S[i-1], self.T[j-1])),
		# 							(self.matrix[i-1][j] + self.gap),
		# 							(self.matrix[i][j-1] + self.gap)
		# 						)

		# 			self.matrix[i][j] = score

		# 			if score == self.matrix[i-1][j-1] + self.score(self.S[i-1], self.T[j-1]):
		# 				self.backtrack[i][j] = (i-1, j-1)

		# 			elif score == self.matrix[i-1][j] + self.gap:
		# 				self.backtrack[i][j] = (i-1, j)

		# 			else:
		# 				self.backtrack[i][j] = (i, j-1)

	def printSemiGlobalAlin(self):

		Saligne = ""
		Taligne = ""
		(i,j) = (self.lS, 0)
		posj_max = -5000000000000000000000000000
		for v in range(self.lT + 1):


			if self.matrix[i][v] > posj_max:
				#print("index : ", v)
				posj_max = self.matrix[i][v]
				j = v

		while (i, j) != (0, 0):
			(fi, fj) = self.backtrack[i][j]
			#print(fi, fj)
			if (fi, fj) == (i - 1, j - 1) : 

				Taligne = self.T[j-1] + Taligne 
				Saligne = self.S[i-1] + Saligne 
			elif fi == i : 
				Taligne = self.T[fj:j] + Taligne
				Saligne = "-" * (j - fj) + Saligne

			elif fj == j: 
				Taligne = "-" * (i - fi) + Taligne
				Saligne = self.S[fi:i] + Saligne

			i = fi
			j = fj
		print(Taligne)
		print(Saligne)

class DMLinearMem():

	def __init__(self, S, T, match, mismatch, gap):
		""" defines and stores initial values """
		self.S = S
		self.T = T
		self.lS = len(S)
		self.lT = len(T)
		self.match = match
		self.mismatch = mismatch
		self.gap = gap
		self.column = [0 for i in range(len(T) + 1)]
		#self.backtrack = [[(0,0) for j in range(len(T)+1)] for i in range(len(S)+1)]


	def score(self, s, t):
		if s == t:
			return self.match
		return self.mismatch

	# def initSemiGlobal(self):

	# 	for i in range(1, self.lS + 1):
	# 		self.row[i] = self.gap * i

	# 	for j in range(1, self.lT + 1):
	# 		self.column[j] = 0

	def fillSemiGlobal(self):
		nb_line=1
		while nb_line != self.lS + 1:
			new_row = [nb_line*self.gap]
			for i in range(1, self.lT):
				score = max (
								self.column[i-1] + self.score(self.S[nb_line-1], self.T[i]),
								self.column[i] + self.gap,
								new_row[i-1] + self.gap
							)
				new_row.append(score)
			self.column = new_row
			nb_line+= 1

		print(self.column)
		print(max(self.column))
