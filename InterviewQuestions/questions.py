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


d = [[0, 1, 10], [2, 4, 20], [1, 1, 15]]
print(CombineDatasets(d))
