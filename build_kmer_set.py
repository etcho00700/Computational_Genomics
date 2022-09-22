def best_fit_kmers(reads, k, skip_len):
    best_fit_set = set()
    edge_set = set()

    for s in reads:
        all_kmers = []
        start_indices = [set()] * (skip_len + 1)
        for i in range(len(s) - k + 1):
            kmer = s[i: i + k]
            all_kmers.append(kmer)
            if kmer in best_fit_set:
                start_indices[i % (skip_len + 1)].add(kmer)

        best_index = 0
        best_val = 0
        for i in range(len(start_indices)):
            intersection = start_indices[i]
            if len(intersection) > best_val:
                best_index = i
                best_val = len(intersection)

        for x in all_kmers[:best_index + 1]:
            edge_set.add(x)

        i = best_index
        last_index = i
        while i < len(all_kmers):
            best_fit_set.add(all_kmers[i])
            last_index = i
            i += skip_len + 1

        for x in all_kmers[last_index:]:
            edge_set.add(x)

    return best_fit_set, edge_set
