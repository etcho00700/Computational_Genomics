import string
import random

# Add any helper functions here

# Generate random kmers of length k and add to false_kmers if not contained
# in the kmers set


def kmer_generator(number, k, kmers, chars='ATCG'):
    false_kmers = set()
    for i in range(number):
        rand_kmer = ''.join(random.choice(chars) for _ in range(k))
        if rand_kmer not in kmers:
            false_kmers.add(rand_kmer)

    return false_kmers
