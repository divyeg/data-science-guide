import loguru as logger


class SortingAlgos(object):
    def __init__(self):
        pass

    def SelectionSort(self, A):
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

    def BubbleSort(self, A):
        """
        This function is used to sort list of arrays using bubble sort sorting algorithm

        """

        for i in range(len(A)):
            for j in reversed(range(i + 1, len(A))):
                if A[j - 1] > A[j]:
                    A[j], A[j - 1] = A[j - 1], A[j]

        return A
