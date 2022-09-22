import bf
import itertools


class KBFSparse(object):
    def __init__(self, size, num_hash, seeds, k, skip_len, kmers, edges):
        self.bf = bf.BloomFilter(size, num_hash, seeds)
        self.k = k  # kmer length
        self.skip_len = skip_len
        self.edge_kmers = set()
        self.num_inserted = 0  # number of kmers inserted

        self.affixes = {}
        self.populate_affixes()

        self.populate(kmers)
        self.getEdges(edges)

    def populate_affixes(self):
        letters = ['A', 'T', 'C', 'G']
        for i in range(1, self.skip_len + 2):
            self.affixes[i] = []
            for x in itertools.combinations_with_replacement(letters, i):
                self.affixes[i].append("".join(x))

    def add(self, kmer):
        self.bf.insert(kmer)
        self.num_inserted += 1

    def populate(self, kmers):
        for kmer in kmers:
            self.add(kmer)

    def getEdges(self, edges):
        for e in edges:
            if e not in self:
                self.edge_kmers.add(e)

    def __contains__(self, kmer) -> bool:
        if kmer in self.bf:
            left = self.skipSearchLeft(kmer, self.skip_len + 1)
            right = self.skipSearchRight(kmer, self.skip_len + 1)
            if left and right:
                return True
            elif left or right:
                if kmer in self.edge_kmers:
                    return True

        for i in range(self.skip_len):
            left = self.skipSearchLeft(kmer, i + 1)
            right = self.skipSearchRight(kmer, self.skip_len - i)
            if left and right:
                return True
            elif left or right:
                if kmer in self.edge_kmers:
                    return True

        return False

    def skipSearchLeft(self, kmer, skip_len):
        suffix = kmer[:-skip_len]
        prefixes = self.affixes[skip_len]

        for p in prefixes:
            if (p + suffix) in self.bf:
                return True
        return False

    def skipSearchRight(self, kmer, skip_len):
        prefix = kmer[skip_len:]
        suffixes = self.affixes[skip_len]

        for s in suffixes:
            if (prefix + s) in self.bf:
                return True
        return False
