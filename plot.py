import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

homedir = os.path.expanduser("~")

plt.rcParams['font.size'] = '14'

def bfsize():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_bfsize.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_bfsize.pkl"))

    bf_size1 = df1['bf_size']
    fpr1 = df1['fpr']
    runtime1 = df1['runtime']

    bf_size2 = df2['bf_size']
    fpr2 = df2['fpr']
    runtime2 = df2['runtime']

    plt.plot(bf_size1, fpr1, '-o', label='sparse_kbf')
    plt.plot(bf_size2, fpr2, '-o', label='1_sided_kbf')
    plt.legend()
    plt.xlabel('filter size (x10^6 elements)')
    plt.ylabel('FPR')
    #plt.plot(bf_size, runtime)
    plt.show()

def bfsize_runtime():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_bfsize.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_bfsize.pkl"))

    bf_size1 = df1['bf_size']
    runtime1 = df1['runtime']

    bf_size2 = df2['bf_size']
    runtime2 = df2['runtime']

    plt.plot(bf_size1, runtime1, '-o')
    plt.plot(bf_size2, runtime2, '-o')
    plt.legend()
    plt.xlabel('filter size (x10^6 elements)')
    plt.ylabel('runtime (s)')
    #plt.plot(bf_size, runtime)
    plt.show()

def num_hashes():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_num_hashes.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_num_hashes.pkl"))

    num_hashes1 = df1["num_hash"]
    fpr1 = df1['fpr']
    num_hashes2 = df2["num_hash"]
    fpr2 = df2['fpr']
    print(df1)

    plt.plot(num_hashes1, fpr1, '-o')
    plt.plot(num_hashes2, fpr2, '-o')
    plt.xlabel("num_hashes")
    plt.ylabel("FPR")
    plt.xticks(range(1,22,2))
    plt.legend()
    plt.show()

def num_hashes_runtime():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_num_hashes.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_num_hashes.pkl"))

    num_hashes1 = df1["num_hash"]
    runtime1 = df1['runtime']
    num_hashes2 = df2["num_hash"]
    runtime2 = df2['runtime']

    plt.plot(num_hashes1, runtime1, '-o')
    plt.plot(num_hashes2, runtime2, '-o')
    plt.xlabel("num_hashes")
    plt.ylabel("runtime (s)")
    plt.xticks(range(1,22,2))
    plt.legend()
    plt.show()

def klen():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_k.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_k.pkl"))

    k1= df1["k"]
    fpr1 = df1['fpr']
    k2 = df2["k"]
    fpr2 = df2['fpr']
    print(df1)
    plt.plot(k1, fpr1, '-o')
    plt.plot(k2, fpr2, '-o')
    plt.xlabel("k length")
    plt.ylabel("FPR")
    plt.legend()
    plt.show()

def klen_runtime():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_k.pkl"))
    df2 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_k.pkl"))

    k1= df1["k"]
    runtime1 = df1['runtime']
    k2 = df2["k"]
    runtime2 = df2['runtime']

    plt.plot(k1, runtime1, '-o')
    plt.plot(k2, runtime2, '-o')
    plt.xlabel("k length")
    plt.ylabel("runtime (s)")
    plt.legend()
    plt.show()

def skiplen():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_skip_len.pkl"))

    skip_len = df1["skip_len"]
    fpr = df1['fpr']

    plt.plot(skip_len, fpr, '-o', label='sparse_kbf')
    plt.xlabel("skip length")
    plt.ylabel("FPR")
    plt.legend()
    plt.show()

def skiplen_runtime():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","sparse_kbf_skip_len.pkl"))
    skip_len = df1["skip_len"]
    runtime = df1['runtime']

    print(df1)
    plt.plot(skip_len, runtime, '-o', label='sparse_kbf')
    plt.xlabel("skip length")
    plt.ylabel("runtime (s)")
    plt.legend()
    plt.show()

def extendlen():
    df1 = pd.read_pickle(os.path.join(homedir, "Desktop","cg_finalproject","results","2sided_kbf_extend_len.pkl"))
    extend_len = df1['extend_len']
    fpr = df1['fpr']
    plt.plot(extend_len, fpr, '-o', label='1sided_kbf')
    plt.xlabel("extend length")
    plt.ylabel("FPR")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    #bfsize()
    #bfsize_runtime()
    #num_hashes()
    #num_hashes_runtime()
    #klen()
    #klen_runtime()
    skiplen()
    #skiplen_runtime()

