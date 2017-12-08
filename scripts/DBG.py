from BloomFilter import BloomFilter

class DBG:
	def __init__(self, fasta_file, kmer_size = 31, bf_size = 6000000000):
		self.fasta_file = str(fasta_file)
		self.kmer_size = kmer_size
		self.bf_size = bf_size
		self.bloom_filter = BloomFilter(bf_size)
		self.nb_kmers = 0
		self.create_DBG()
		self.comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
	
	def create_DBG(self):
		""" Faire attention au if line[0] == '>'""" 
		with open(self.fasta_file , 'r') as input_data:
		
			next(input_data)
			for line in input_data:
				line = line.rstrip().upper()
				# change pas trop le temps car on a qu'une seul ligne dans le fichier qui commence avec >
				if line[0] == '>' : continue 
				for i in range(len(line) - self.kmer_size + 1):
					kmer = line[len(line) - self.kmer_size - i:len(line) - i]
					#print kmer
					cr = self.canonical(kmer)
					self.bloom_filter.add_word(cr)
					self.nb_kmers += 1
					
	def canonical(self, kmer):
		reverse_kmer = ""
		for aa in kmer[::-1]:
			reverse_kmer+= self.comp[aa]
		
		if kmer < reverse_kmer:
			return kmer
		return reverse_kmer
				


#			self.bloom_filter.add_word("TGGA")
#			self.bloom_filter.add_word("GGAA")
#			self.bloom_filter.add_word("GAAT")
#			self.bloom_filter.add_word("TGGG")
#			self.bloom_filter.add_word("GGGT")
#			for line in input_data:
#				line = line.rstrip().split()[1].upper()
#				if line[0] == '>' : continue 
#				self.bloom_filter.add_word(line)
#				self.nb_kmers += 1

