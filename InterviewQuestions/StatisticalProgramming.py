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
    We will use random.random() and classify it as H if it is less than or equal to 0.7 and T if it
    is greater than 0.7. We will toss this coin twice to get the fair coin.
    H, H = 0.49
    H, T = 0.21 - Heads
    T, H = 0.21 - Tails
    T, T = 0.09
    The efficiency of the system is 42%, we can improve this efficiency by considering H,H and T,T
    scenarios from two coin toss which basically means instead of throwing aways these cases we couple
    these cases with HT, HH and TT cases to improve efficiency.
    H,H H,H = 0.49 * 0.49
    H,H H,T = 0.49 * 0.21 - Heads
    H,H T,T = 0.49 * 0.09 - Heads
    T,T H,T = 0.09 * 0.21 - Heads
    H,H T,H = 0.49 * 0.21 - Tails
    T,T H,H = 0.09 * 0.49 - Tails
    T,T T,H = 0.09 * 0.21 - Tails
    T,T T,T = 0.09 * 0.09
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

"""
Q3: Given a base a and an exponent b. Your task is to find a^b. The value could be large enough. 
So, calculate a^b % 1000000007.
"""

"""
Solution: Figure out the edges case and write them first. Edge cases include when b = 0, then return 1, 
when a = 1, then return 1 and when a = 0, then return 0. if b is odd, then multiply the result by a to 
account for additional a, else multiply result by itself.
"""


def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    if b == 0:
        return 1
    if a == 1:
        return 1
    if a == 0:
        return 0

    result = calculate_power(a, b // 2)
    result_power = (result * result) % 1000000007

    if b % 2 > 0:
        result_power = (result_power * a) % 1000000007
        return result_power
    else:
        return result_power


"""
Q4: Write a function to calculate empirical cumulative distribution function given an array and number 
of bins
"""

"""
Solution: We start with sorting the array and finding mix and max values. We then calculate bin_width.
We then define the left bin value and right bin value for each nums in x taking care of cases where
right bin value never exceeds the max value of nums in x.
"""


def cumulative_distribution_function(x, bins):
    """
    The function is used to calculate the empirical cumulative distribution function for a data distribution
    """
    x = sorted(x)
    max_x = max(x)
    min_x = min(x)
    bin_width = (max_x - min_x) // bins
    ecdf = {}
    for nums in x:
        bin_number = (nums - min_x) // (bin_width + 1)
        bin_l = min_x + (bin_number) * (bin_width + 1)
        if bin_l >= max_x:
            bin_l = max_x
        bin_r = bin_l + (bin_width)
        if bin_r >= max_x:
            bin_r = max_x
        bin_name = f"{bin_l} - {bin_r}"
        if bin_name in ecdf.keys():
            ecdf[bin_name] += 1
        else:
            ecdf[bin_name] = 1
    return ecdf
