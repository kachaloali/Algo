from BitArray import BitArray
from kmer2hash import kmer2hash

class BloomFilter:
	def __init__(self, size, nb_hashs=7): #par defaut 7 si l'utilisateur ne precise pas
		""" Question 6 size et nombre de fonction de hashage"""
		self.BitArray = BitArray(size)
		self.nb_hashs = nb_hashs


	def add_word(self, word):
		for i in range(self.nb_hashs):
			adress = kmer2hash(word, i) % self.BitArray.size
			self.BitArray.set_i(adress)
	
	def remove_word(self, word):
		for i in range(self.nb_hashs):
			adress = kmer2hash(word, i) % self.BitArray.size
			self.BitArray.remove_i(adress)	

	def exists_word(self, word):
		for i in range(self.nb_hashs):
			adress = kmer2hash(word, i) % self.BitArray.size
			
			if not self.BitArray.get_i(adress): return False
		return True
