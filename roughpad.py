from loguru import logger
import numpy


def quicksort(A):
    """
    This function is used to sort an array using quick sort algorithm

    """
    if len(A) <= 1:
        return A
    pivot = numpy.random.randint(1, len(A))
    p1 = 0
    p2 = len(A) - 1
    A[pivot], A[p2] = A[p2], A[pivot]
    pivot = p2
    p2 = p2 - 1
    while p1 <= p2:
        if A[p1] <= A[pivot]:
            p1 = p1 + 1
        else:
            A[p1], A[p2] = A[p2], A[p1]
            p2 = p2 - 1

    A[p1], A[pivot] = A[pivot], A[p1]
    A1 = quicksort(A[:p1])
    A2 = quicksort(A[p1 + 1 :])
    A = A1 + [A[p1]] + A2

    return A


A = [7, 5, 1, 3, 9]
print(quicksort(A))
