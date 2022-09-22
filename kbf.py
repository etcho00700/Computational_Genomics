import bf


class KmerBloomFilter(object):
    def __init__(self, size, num_hash, seeds, k, kmers, extend_len):
        self.kmerbf = bf.BloomFilter(
            size, num_hash, seeds)  # basic bloom filter
        self.k = k  # kmer length
        self.num_inserted = 0  # number of kmers inserted
        self.populate(kmers)
        self.extend_len = extend_len

    def add(self, kmer):
        self.kmerbf.insert(kmer)
        self.num_inserted += 1

    def __contains__(self, kmer) -> bool:
        if kmer not in self.kmerbf:
            return False
        else:
            if self.extend_len == 0:
                return True
            left = self.searchLeft(kmer, self.extend_len, self.k, self.kmerbf)
            right = self.searchRight(
                kmer, self.extend_len, self.k, self.kmerbf)
            if right or left:
                return True
        return False

    def populate(self, kmers):
        for kmer in kmers:
            self.add(kmer)

    def searchLeft(self, kmer, len, k, bf):
        if len == 0:
            return False
        contains = False
        suffix = kmer[:-1]
        nts = ['A', 'C', 'G', 'T']

        for nt in nts:
            if (nt + suffix) in bf:
                return True
            else:
                contains = self.searchLeft(suffix, len - 1, k, bf)
            if contains:
                return contains

        return contains

    def searchRight(self, kmer, len, k, bf):
        if len == 0:
            return False
        contains = False
        prefix = kmer[1:]
        nts = ['A', 'C', 'G', 'T']

        for nt in nts:
            if (prefix + nt) in bf:
                return True
            else:
                contains = self.searchRight(prefix, len - 1, k, bf)
            if contains:
                return contains

        return contains
