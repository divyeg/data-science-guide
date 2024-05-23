import random
import numpy as np

"""
Q1: Suppose you are given K datasets with mean and variance. Write a function that can give 
mean and variance of the combined datasets
"""

"""
Solution: We will use merge sort algorithm to recursively combine two datasets. Helper function 
will contain the code for combining 2 datasets. Math of mean and variance is done on paper.
"""


def Combine2Datasets(d1, d2):
    """
    d1 is a list of dataset 1 that contains mean, variance and number of observations
    """

    x1, s1, n1 = d1[0], d1[1], d1[2]
    x2, s2, n2 = d2[0], d2[1], d2[2]

    if n1 == 0:
        return d2
    if n2 == 0:
        return d1

    x = (n1 * x1 + n2 * x2) / (n1 + n2)
    s = n1 * s1 + n2 * s2 + n1 * x1 * x1 + n2 * x2 * x2 - ((n1 + n2) * x * x)
    n = n1 + n2

    return [x, s, n]


def CombineDatasets(d):
    """
    d is a list of datasets where each element is a list containing mean, variance and
    number of observations
    """
    if len(d) == 0:
        return None
    if len(d) == 1:
        return d[0]

    m = round(len(d) / 2)
    d1 = CombineDatasets(d[:m])
    d2 = CombineDatasets(d[m:])

    result = Combine2Datasets(d1, d2)
    return result


# d = [[0, 1, 10], [2, 4, 20], [1, 1, 15]]
# print(CombineDatasets(d))


"""
Q2: Let's say you have a biased coin which has probability of showing head as 0.7. Write a function 
that simulates a fair coin. Calculate the efficiency of this system and how will you improve the 
efficiency of this system?
"""

"""
Solution: In order to covert a biased coin to a fair coin, we will map the multiple coin tosses to 
fair coin's head and tail. For example, when we toss a biased coin twice, p(H,T) = p(T, H). Hence we 
can map H,T as H and T,H as T and discount whenever the coin shows HH or TT. 
"""


def CoinToss(p):
    toss = random.random()
    if toss <= p:
        return "H"
    else:
        return "T"


def SimulateFairCoin(N, p1, p2):
    """
    we will use random.random() and classify it as H if it is less than or equal to 0.7 and T if it
    is greater than 0.7. We will toss this coin twice to get the fair coin.
    H, H = 0.49
    H, T = 0.21
    T, H = 0.21
    T, T = 0.09
    """
    i = 0
    result = []
    while i <= N:
        toss = (CoinToss(p1), CoinToss(p2))
        if toss == ("H", "T"):
            result.append("H")
            i += 1
        if toss == ("T", "H"):
            result.append("T")
            i += 1
    return result


def RunSimulation(N, p1, p2):
    result = SimulateFairCoin(N, p1, p2)
    counter = [0] * 2
    i = 0
    while i < len(result):
        if result[i] == "H":
            counter[0] += 1
        else:
            counter[1] += 1
        i += 1
    counter = [x / len(result) for x in counter]
    print(counter)


# RunSimulation(1000, 0.7, 0.7)
