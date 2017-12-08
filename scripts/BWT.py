import tools_karkkainen_sanders as tks

class BWT:
	def __init__(self, T):
		self.SA = self.get_SA(T + "$")
		self.BWT = self.get_BWT(T + "$", self.SA)	
		self.N = self.get_N(self.BWT)
		self.R = self.get_R(self.BWT)	
		
	def get_SA(self, T):
		n = len(T)
		sa = tks.simple_kark_sort(T)[:-3]
		res = []
		for i in xrange(n):
			res.append(sa[i])
		return res

	def get_BWT(self, T, SA):
		res = []
		for i in xrange(len(SA)):
			if SA[i] > 0:
				res.append(T[SA[i]-1])
			else:
				res.append('$')
		return res
	
	def BWT2SEQ(self):
		i = 0
		T = self.BWT[0]
		while True:
			next_line = self.LF(self.R[i], self.BWT[i])	
			if self.BWT[next_line] == '$':
				return T
			else:
				T = self.BWT[next_line] + T
			i = next_line

	
	def get_N(self, BWT):
		_dico  = {'A': 0, 'C': 0, 'G': 0, 'T': 0,'$': 0 }
		for i in BWT:
			_dico[i] = _dico[i] + 1
		return _dico

	def get_R(self, BWT):
		_dico = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '$': 0 }
		rank = []
	
		for i in BWT:
			_dico[i] = _dico[i] + 1
			rank.append(_dico[i])
		return rank
		
	def LF(self, k, alpha):
		_list = ['$','A','C','G','T']
		index = _list.index(alpha)
		_sum = 0
		for i in range(index):
			_sum+= self.N[_list[i]]
		return _sum + k-1
	
	def exist_pattern(self, P):
		i, j = 0, len(self.BWT)-1
		indexes = range(len(P))
		indexes.reverse()
		
		for posQ in indexes:
			current_char = P[posQ]
			positions = []
			for x in range(i, j+1):
				if self.BWT[x] == current_char:
					positions.append(x)
			try:
				i_prim = min(positions)
			except:
				return False
			
			j_prim = max(positions)
			i = self.LF(self.R[i_prim], self.BWT[i_prim])
			j = self.LF(self.R[j_prim], self.BWT[j_prim])
		return True	
	
	def where_is_pattern(self, P):
		pos, i, j = 0, 0, len(self.BWT)-1
		indexes = range(len(P))
		indexes.reverse()
		
		for posQ in indexes:
			current_char = P[posQ]
			positions = []
			for x in range(i, j+1):
				if self.BWT[x] == current_char:
					positions.append(x)
			try:
				i_prim = min(positions)
			except:
				return None
			
			j_prim = max(positions)
			i = self.LF(self.R[i_prim], self.BWT[i_prim])
			j = self.LF(self.R[j_prim], self.BWT[j_prim])
			pos = i 
		return self.SA[pos:j+1]
	
	
