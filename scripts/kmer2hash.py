char2bitstr={"A":"00","C":"01","G":"10","T":"11"}
#char2bitstr2={"A":"0","C":"1","G":"1","T":"0"}
#char2bit={"A":'0b00',"C":'0b01',"G":'0b10',"T":'0b11'}
#char2int={"A":0,"C":1,"G":2,"T":3}

def kmer2hash(kmer,seed):
    key=int('0b' + ''.join([char2bitstr[c] for c in kmer]), 2)
    hash=seed
    hash ^= (hash <<  7) ^  key * (hash >> 3) ^ (~((hash << 11) + (key ^ (hash >> 5))));
    hash = (~hash) + (hash << 21);
    hash = hash ^ (hash >> 24);
    hash = (hash + (hash << 3)) + (hash << 8);
    hash = hash ^ (hash >> 14);
    hash = (hash + (hash << 2)) + (hash << 4);
    hash = hash ^ (hash >> 28);
    hash = hash + (hash << 31);
    return hash