import sys
import time

from DBG import DBG
from BWT import BWT
from Contiger import Contiger
from Mapper import DMLinearMem
from Mapper import DynamicMatrix
import tools_karkkainen_sanders as tks
#sys.stdout = open("log_file.log", "w")



genome_ref_file = "../mapping-test1/reference1.fasta"
target_kmers_file = "../mapping-test1/reads.fasta"
contigs_file_out = "contigs_out.fa"

#test DBG
print "********************************************************************************************"
print "{}".format("Creating Bruijn Graph...")
start_time = time.time()
dbg = DBG(genome_ref_file)
elasped_time = time.time() - start_time

print "{:>10} : {}".format("input file", genome_ref_file)
print "{:>10} : {}".format("kmers size", dbg.kmer_size)
print "{:>10} : {}".format("bloom filter size", dbg.bf_size)
print "{:>10} : {}".format("number of kmers", dbg.nb_kmers)
print "{:>10} : {}".format("execution time", elasped_time)
print "{:>10} : {}".format("Run","Success")
print ""



#test contiger
print "********************************************************************************************"
contiger = Contiger(dbg)

print "{}".format("Writing generate contigs from the target kmers file...")
print ""
try:
	target_kmers = open(target_kmers_file, "r")
	f = open(contigs_file_out, "w")
except:
	print "{}".format("ERROR: Missing target kmers file...")

for line in target_kmers:
	if line[0] == ">":
		continue
	else:
		text = contiger.generate_contig(line.rstrip(), 2)
		text+= "\n"
		f.write(text )
f.close()
target_kmers.close()


#test mapping
print "********************************************************************************************"
print ""
print "{}".format("Starting mapping...")
gap = -2
match = 3
mismatch = -1

print ""
print "gap: ", gap
print "match: ", match
print "mismatch: ", mismatch
print ""

with open(genome_ref_file , 'r') as input_data:
	next(input_data)
	for line in input_data:
		genome_ref = line.rstrip().upper()
	contigs_file = open(contigs_file_out, 'r')
	i = 0
	print "{}".format("Printing scores of alignment for each contig...")	
#	for s in contigs_file:
#		if s.rstrip() != "":
#			print '>: contig: ', i+1
#			mapper = DynamicMatrix(s, t, match, mismatch, gap)
#			i+= 1
#			print "\n"
#=======================================================================
print "********************************************************************************************"
		
#test BWT for indexing genome
BWT = BWT(genome_ref)
target_kmers = open(target_kmers_file, "r")
k = BWT.kmer_size
for line in target_kmers:
	if line[0] == ">":
		continue
	else:
		read = line.rstrip().upper()
		if BWT.exist_pattern(read):
			print "True"
		else:
			read_size = len(read)
			for i in range(read_size - k + 1):
				seed = read[read_size - k - i:read_size - i]
				if BWT.exist_pattern(seed):
					print seed
			exit(0)
target_kmers.close()	


print ""
#print "exist_pattern \n", BWT.exist_pattern(P)
#print "where_is_pattern\n", BWT.where_is_pattern(P)	
print "\tFinished..."


#***************************************************************************************************
#kmer_starter = "GAACAACTGGCCGCGTGTGGAAGAGTTGTTC"
#print contiger.dbg.bloom_filter.exists_word("TGGG")
#contiger.remove_tips(kmer_starter, 2)
#print contiger.dbg.bloom_filter.exists_word("GGGT")


#right_unitig = contiger.extend_right_kmer(kmer_starter)
#print "{:>10} : {}".format("extend_right_kmer", right_unitig)
#print "{:>10} : {}".format("extend_left_kmer", contiger.extend_left_kmer(kmer_starter))
#print "{:>10} : {}".format("genrate_unitig", contiger.genrate_unitig(kmer_starter))

#right_contig=contiger.generate_right_contig(right_unitig[len(right_unitig)-len(kmer_starter):], 2)
#left_contig = contiger.generate_left_contig(kmer_starter, 2)
#contig = contiger.generate_contig(kmer_starter, 2)
#print "{:>10} : {}".format("right_contig", right_contig)
#print "{:>10} : {}".format("left_contig", left_contig)
#print "{:>10} : {}".format("contig", contig)

#print "{:>10} : {}".format("extend_left_kmer", contiger.extend_left_kmer_reverse(kmer_starter))

#print "reverse_comp", contiger.reverse_comp(kmer_starter)




