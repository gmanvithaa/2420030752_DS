import pandas as pd
import numpy as np
from scipy.stats import spearmanr

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Strings must be of the same length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(str1, str2))
hamming_dist = hamming_distance("abcd", "efgh")
print("Hamming Distance:", hamming_dist)
