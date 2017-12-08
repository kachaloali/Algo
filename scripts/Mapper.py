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
		self.fillSemiGlobal()
		self.printSemiGlobalAlin()
	
	def initSemiGlobal(self):
		for i in range(1, self.lS+1):
			self.matrix[i][0] = self.gap * i
			
		for j in range(1, self.lT + 1):
			self.matrix[0][j] = 0
	
	def score(self, s, t):
		if s == t:
			return self.match
		return self.mismatch
		
	def fillGlobal(self):
		for i in range(1, self.lS + 1):
			for j in range(1, self.lT + 1):
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
	
	def fillSemiGlobal(self):
		self.fillGlobal()
					
	
	def printSemiGlobalAlin(self):
		Saligne = ""
		Taligne = ""
		(i, j) = (self.lS, 0)
		posj_max = -5000000000000000000000000000
		
		for k in range(self.lT + 1):
			if self.matrix[i][k] > posj_max:
				posj_max = self.matrix[i][k]
				j = k

		while (i, j) != (0, 0):
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
		self.score = self.fillSemiGlobal()
		self.printScore()

		
	
	def printScore(self):
		print self.score
		
	def score(self, s, t):
		if s == t:
			return self.match
		return self.mismatch

	def fillSemiGlobal(self):
		nb_line = 1
		while nb_line != self.lS + 1:
			new_row = [nb_line*self.gap]
			for i in range(1, self.lT):
				score = max (
					self.column[i-1] + self.score(self.S[nb_line - 1], self.T[i]),
					self.column[i] + self.gap,
					new_row[i-1] + self.gap
				)
				new_row.append(score)
			self.column = new_row
			nb_line+= 1
		return max(self.column)
