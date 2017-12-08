class BitArray:

	def __init__(self, size):
		""" Question 3 """
		self.size = size
		self.bf_array = bytearray(1 + size//8)
		""" Tableau d'octet"""

	def __str__ (self):
		a = ""
		for i in self.bf_array:
			bit = "0"
			if self.set_i(i): 
				bit = "1"
			a += bit
		return a
		# a = [str(i) for i in self.bloom_array]
		# return "".join(a)

	def set_i(self, positionBit):
		""" Question 4
			Exemple avec position de 5
		"""
		octet_id = positionBit//8
		position_on_octet = positionBit % 8
		#old_octet = self.array[octect_id] #0000 0000
		#on doit creer 0000 1000
		new_octet = 1 << position_on_octet
		# 1 creer octet 0000 0001
		# << 4 donne 0001 0000 decaler de 4 zeros
		# 5eme bit est a 1


		"""
			Exemple :

			avant					0010 0101
			my_new_octet			0001 0000
									---------
								ou: 0011 0101	
		"""


		self.bf_array[octet_id] = self.bf_array[octet_id] | new_octet

		# on peut tt ecrire en 1 seule fois : self.bloom_array[positionBit//8]|=1<<positionBit%8
		# // reste entier de la division
	
	def remove_i(self, positionBit):
		octet_id = positionBit//8
		position_on_octet = positionBit % 8
		new_octet = 0 << position_on_octet
		self.bf_array[octet_id] = self.bf_array[octet_id] & new_octet


	def get_i(self, positionBit):
		""" Question 5"""

		octet_id = positionBit//8
		position_on_octet = positionBit % 8
		new_octet = 1 << position_on_octet

		test = self.bf_array[octet_id] & new_octet

		return test != 0

		""" 
		if positionBit > self.size:
			exit(0)
		octet_id=positionBit//8
		position_on_octet = positionBit % 8
		mask = 1 << position_on_octet

		if self.array[] &mask !=0 return Trrue
		else: return False

		"""
