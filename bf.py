import xxhash
import sys


def get_words(filename):
    return open(filename, "rb").read().decode("utf8", "ignore").strip().split()


class HashXX32(object):
    def __init__(self, seed):
        self.h = xxhash.xxh32(seed=seed)

    def hash(self, o):
        self.h.reset()
        self.h.update(o)
        return self.h.intdigest() % sys.maxsize


class BloomFilter(object):
    def __init__(self, size, num_hash, seeds):
        '''
        Initialize a Bloom filter.

        Inputs:
            - size: number of slots in the Bloom filter (n)
            - num_hash: number of hash functions (k)
            - seeds: seeds to initialize hash functions

        Raises:
            - ValueError if the number of seeds differ with num_hash
        '''
        self._size = size
        self._num_hash = num_hash
        self._hashers = [HashXX32(seed) for seed in seeds]
        if num_hash != len(self._hashers):
            raise ValueError(
                'Number of hash functions should equal number of seeds.')
        self._bits = [0 for i in range(size)]

    def insert(self, obj) -> int:
        '''
        Insert an object into the Bloom filter.
        The object will be hashed with `self._num_hash` distinct hash functions.

        Inputs:
            - obj: a bytes-like object.

        Returns:
            - num_collision (int): number of collisions during this insertion operation.
        '''
        num_collision = 0
        for i in range(self._num_hash):
            index = self._hashers[i].hash(obj) % self._size
            if self._bits[index] == 1:
                num_collision += 1
            else:
                self._bits[index] = 1
        return num_collision

    def __contains__(self, obj) -> bool:
        '''
        Check if an object is in the Bloom filter.

        Inputs:
            - obj: a bytes-like object.

        Returns:
            True if `obj` is in the filter; otherwise False.
        '''
        for i in range(self._num_hash):
            index = self._hashers[i].hash(obj) % self._size
            if self._bits[index] == 0:
                return False
        return True

    def get_num_set_buckets(self) -> int:
        '''Return the number of set buckets in the Bloom filter.'''
        return sum(self._bits)

    def get_bit_vector(self):
        return ''.join([str(b*1) for b in self._bits])


def bf_insertion(bf, members):
    num_collision = 0
    for word in members:
        num_collision += bf.insert(word)
    return num_collision


if __name__ == '__main__':
    words = [str(i) for i in range(10000)]
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    num_hash = int(sys.argv[3])
    bf_size = int(sys.argv[4])

    bf = BloomFilter(size=bf_size, num_hash=num_hash, seeds=range(num_hash))
    members = words[start: end]

    print(bf_insertion(bf, members))
    print(bf.get_bit_vector())
