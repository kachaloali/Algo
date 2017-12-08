class Contiger:
	def __init__(self, dbg):
		""""""
		self.dbg = dbg
		self.comp = {"A": "T", "T": "A", "G": "C", "C": "G"}
		
	def get_right_child(self, kmer_starter):
			right_child = []
			
			for aa in ['A','C','G','T']:
#				if self.dbg.bloom_filter.exists_word(kmer_starter[1:] + aa):
#					right_child.append(aa)
				
				if self.dbg.bloom_filter.exists_word(canonical(kmer_starter[1:] + aa)):
					right_child.append(aa)
					
			return right_child
			
	def get_left_child(self, kmer_starter):
			left_child = []
			
			for aa in ['A','C','G','T']:
				if self.dbg.bloom_filter.exists_word(aa + kmer_starter[:len(kmer_starter)-1]):
					left_child.append(aa)
			return left_child

	def extend_right_kmer(self, kmer_starter):
		unitig = kmer_starter
		
		while True:
			successors = self.get_right_child(kmer_starter)
			if len(successors) != 1 : break
			kmer_starter = kmer_starter[1:] + successors[0]
			unitig += successors[0]
		return unitig
		

	def extend_left_kmer_reverse(self, kmer_starter):
		return self.reverse_comp(self.extend_right_kmer(self.reverse_comp(kmer_starter)))
	
	def extend_left_kmer(self, kmer_starter):
		kmer_starter = kmer_starter
		unitig = kmer_starter
		
		while True:
			predecessors = self.get_left_child(kmer_starter)
			if len(predecessors) != 1 : break
			kmer_starter = predecessors[0] + kmer_starter[:len(kmer_starter) - 1]
			unitig = predecessors[0] + unitig
		return unitig
	
	def remove_tips(self, kmer_starter, tip_size):
		right_childs = self.get_right_child(kmer_starter)
		if len(right_childs) > 1:
			for aa in right_childs:
				unitig = kmer_starter[0]
				unitig += self.extend_right_kmer(kmer_starter[1:] + aa)
				if len(unitig) == len(kmer_starter) + tip_size:
					for i in range(1, tip_size + 1):
						kmer = unitig[i:len(kmer_starter) + i]
						print kmer
						self.dbg.bloom_filter.remove_word(kmer)
	
	def genrate_unitig(self, kmer_starter):
		left_unitig = self.extend_left_kmer(kmer_starter)
		right_unitig = self.extend_right_kmer(kmer_starter)
		return  left_unitig[:-len(kmer_starter)] + right_unitig 
		
	def generate_right_contig(self, kmer_starter, larger):
		right_childs = self.get_right_child(kmer_starter)
		right_unitigs = {}
		
		if (len(right_childs) < 1 or len(right_childs) > larger):
			return kmer_starter
		
		for aa in right_childs:
			right_unitigs[aa] = kmer_starter[0] + self.extend_right_kmer(kmer_starter[1:] + aa)
			
		for i in range(len(right_childs) - 1):
			first_aa = right_childs[i]
			snd_aa = right_childs[i + 1]
			first_unitig = right_unitigs[first_aa]
			snd_unitig = right_unitigs[snd_aa]
			
			if first_unitig[len(first_unitig) - len(kmer_starter):] != snd_unitig[len(snd_unitig) - len(kmer_starter):]:
				return kmer_starter
				
		aa_with_max_unitig = max(right_unitigs.keys(), key = lambda aa: len(right_unitigs[aa]))
		max_right_unitig = right_unitigs[aa_with_max_unitig]
		return max_right_unitig
	
	def generate_left_contig(self, kmer_starter, larger):
		left_childs = self.get_left_child(kmer_starter)
		left_unitigs = {}
		
		if (len(left_childs) < 1 or len(left_childs) > larger):
			return kmer_starter
			
		for aa in left_childs:
			left_unitigs[aa] = self.extend_left_kmer(aa + kmer_starter[:-1]) + kmer_starter[len(kmer_starter) - 1:]
		
		for i in range(len(left_childs) - 1):
			first_aa = left_childs[i]
			snd_aa = left_childs[i + 1]
			first_unitig = left_unitigs[first_aa]
			snd_unitig = left_unitigs[snd_aa]
			
			if first_unitig[:len(kmer_starter)] != snd_unitig[:len(kmer_starter)]:
				return kmer_starter
		aa_with_max_unitig = max(left_unitigs.keys(), key = lambda aa: len(left_unitigs[aa]))
		max_left_unitig = left_unitigs[aa_with_max_unitig]
		return max_left_unitig
	
	
	def generate_contig(self, kmer_starter, larger):
		right_contig = self.generate_right_contig(kmer_starter, larger)
		left_contig = self.generate_left_contig(kmer_starter, larger)
		
		if right_contig == kmer_starter:
			return left_contig
		elif left_contig == kmer_starter:
			return right_contig
		else:
			right_kmer_starter = right_contig[len(right_contig) - len(kmer_starter):]
			left_kmer_starter = left_contig[:len(kmer_starter)]
			return (self.generate_contig(left_kmer_starter, larger)[:-len(left_kmer_starter)]
			+ left_contig[:-len(kmer_starter)]+right_contig[:-len(kmer_starter)]
			+ self.generate_right_contig(right_kmer_starter, larger))



	def canonical(self, kmer):
		reverse_kmer = ""
		for aa in kmer[::-1]:
			reverse_kmer = reverse_kmer + self.comp[aa]
		if kmer < reverse_kmer:
			return kmer
		return reverse_kmer
	
	def canonical_representation(self, kmer):
		rc = self.reverse_complement(kmer)
		if rc < kmer: return rc
		return kmer
		
	def reverse_comp(self, seq):
		return ("".join(self.comp[char] for char in seq))[::-1]
	

#	def extend_left_kmer_reverse(self, kmer_starter):
#		reverse_kmer = self.reverse_comp(kmer_starter)
#		unitig = reverse_kmer
#		while True:
#			pred = self.get_right_child(reverse_kmer)
#			if len(pred) != 1: break
#			reverse_kmer = reverse_kmer[1:] + pred[0]
#			unitig += pred[0]
#		return self.reverse_comp(unitig)



#		print "contigs", right_unitigs
#		for aa in right_unitigs:
#			right_unitig = right_unitigs[aa]
#			kmer_starter0 = right_unitig[len(right_unitig) - len(kmer_starter):]
#			right_unitigs[aa] += self.generate_right_contig(kmer_starter0, larger)

