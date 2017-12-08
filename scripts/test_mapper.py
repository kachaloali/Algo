from DBG import DBG
from BWT import BWT
from Contiger import Contiger
genome_ref_file = "genome_ref_file.fasta"


dbg = DBG(genome_ref_file, 4)
contiger = Contiger(dbg)

print("genome_ref_file")
print "TGACTGGCAATCG"


print "extend_right_kmer\n", contiger.extend_right_kmer("CTGG")
print "extend_left_kmer\n", contiger.extend_left_kmer("CTGG")
print "extend_left_kmer_reverse\n", contiger.extend_left_kmer_reverse("CTGG")
