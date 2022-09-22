'''
20211111 Computational Genomics Final Project
This code is the main function used to test parameters in optimizing our Bloom
Filter (BF). We are using a sparse BF.

Additional files needed for this main:
    1. bf.py
    2. kbf.py
    3. kmer.py
    4. sparse_kbf.py
'''

import bf
import kbf
import build_kmer_set
import sparse_kbf
import sys
import time
import helper


def parse_fastq(fh):
    '''
    Parse reads from a FASTQ filehandle. For each read, return a name,
    nucleotide-string, quality-string triple.

    Taken from Professor Langmead.
    '''
    reads = []
    while True:
        first_line = fh.readline()
        if len(first_line) == 0:
            break  # end of file
        name = first_line[1:].rstrip()
        seq = fh.readline().rstrip()
        fh.readline()  # ignore line starting with +
        qual = fh.readline().rstrip()
        reads.append(seq)  # we only care about sequences
    return reads


if __name__ == '__main__':
    # parameters to take from command line later on
    fn = './Data/readA.fastq'
    size = 5000000
    num_hash = 6
    k = 20
    skip_len = 7

    fh = open(fn, 'r')
    fastq_reads = parse_fastq(fh)  # parse fastq file to get just reads

    # querying
    kmers = set()
    for read in fastq_reads:
        for i in range(len(read) - k + 1):  # for each k-mer
            kmer = read[i:i + k]
            kmers.add(kmer)

    false_kmers = list(helper.kmer_generator(100000, k, kmers))

    start = time.time()

    # populate sparse bloom filter
    best_fit_set, edge_set = build_kmer_set.best_fit_kmers(
        fastq_reads, k, skip_len)
    KBFSparse = sparse_kbf.KBFSparse(size, num_hash, range(
        num_hash), k, skip_len, best_fit_set, edge_set)

    true_negative = 0
    false_positive = 0
    for kmer in false_kmers:
        if kmer in KBFSparse:
            false_positive += 1
        else:
            true_negative += 1
    print(f"TN: {true_negative}\nFP: {false_positive}\n")

    end = time.time()
    print(f"Runtime for {len(false_kmers)} queries: {end - start} seconds")
