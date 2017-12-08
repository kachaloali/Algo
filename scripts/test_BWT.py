from BWT import BWT
import tools_karkkainen_sanders as tks
T = "GAACAACTGGCCGCGTGTGGAAGAGTTGTTC$"
P = "AA"
BWT = BWT(T)
print "T", T
print "len(T)", len(T)
print "sa", tks.simple_kark_sort(T)[:-3]
print "BWT.SA: ", BWT.SA
print "len(BWT.SA)", len(BWT.SA)
print "get_R", BWT.R
print "BWT", BWT.BWT
print "BWT.N", BWT.N
print "exist_pattern\n", BWT.exist_pattern(P)
print "where_is_pattern\n", BWT.where_is_pattern(P)


#print BWT.exist_pattern("GCGTGT")
#print BWT.BWT2SEQ()
