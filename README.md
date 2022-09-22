# Computational Genomics Final Project 
## Authors: Arpan Sahoo, Christine Hwang, Evan Leung, Eun Tack Cho
## Instructions
*The python scripts necessary to run the experiments are in the root directory. No further change is needed. 

*The sequence files are located in the ./Data directory. There may be subdirectories inside ./Data but they are
specified in the jupyter notebook, and no further change is required. 

1. Please open the cg_finalproject folder, and open parameter_experiment.ipynb and sequence_experiment.ipynb on a jupyter notebook. Standard python3 kernels should be used. 

2. In order to run the experiment 1 (parameter sweep) from the paper, follow the instructions in parameter_experiment.ipynb. Run the cells from the beginning sequentially, which runs all the import statements, function definitions, and main functions. At the end, it should reproduce all figures displayed in the experiment 1 section. 

3. In order to run the experiment 2 (sequence matching) from the paper, follow the instructions in sequence_experiment.ipynb. Run the cells from the beginning sequentially. At the end, it should reproduce all tables displayed in the experiment 2 section.

## Scripts
1. bf.py: Basic bloom filter implementation. Used as the parent class that kbf.py and sparse_kbf.py inherit from.
2. kbf.py: Implementation of the 1-sided kBF. Implements the initialization of a 1-kBF, populate, searchLeft(), and searchRight() functions for kmer query. 
3. sparse_kbf.py: Implementation of the sparse kBF. Implements the initialization of a sparse-kBF, populate, skipSearchLeft(), and skipSearchRight() for kmer query. 
4. build_kmer_set.py: builds the best_fit_kmers set to generate input for sparse_kbf. 
5. main.py: main function to test the filters. This file does not need to run, as main functions for experiment 1 and experiment 2 are implemented in parameter_experiment.ipynb and sequence_experiment.ipynb, respectively. 
6. helper.py: helper functions
7. plot.py: plot functions used to generate figures

We referenced the code written by the Kingsford-Group. Can be accessed at:
https://github.com/Kingsford-Group/kbf

Pellow, David, et al. “Improving Bloom Filter Performance on Sequence Data Using k-mer Bloom Filters.” Journal of Computational Biology, vol. 24, no. 6, 2017, https://www.ncbi.nlm.nih.gov/labs/pmc/articles/PMC5467106/pdf/cmb.2016.0155.pdf.