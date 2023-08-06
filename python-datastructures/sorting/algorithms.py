import loguru as logger


class SortingAlgos(object):
    def __init__(self):
        pass

    def SelectionSort(A):
        """
        This function is used to sort list of arrays using brute force sorting algorithm

        """
        for i in range(len(A)):
            min_value = A[i]
            min_index = i
            for j in range(i + 1, len(A)):
                if A[j] < min_value:
                    min_value = A[j]
                    min_index = j

            A[i], A[min_index] = A[min_index], A[i]

        logger.debug(f"Sorting Array is completed using brute force algorithm")
        return A
