import loguru as logger
import numpy


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
        This function is used to sort list using bubble sort sorting algorithm
        Explanation: We start with last element of the list and move it up if it is less than left element

        """

        for i in range(len(A)):
            for j in reversed(range(i + 1, len(A))):
                if A[j - 1] > A[j]:
                    A[j], A[j - 1] = A[j - 1], A[j]

        return A

    def InsertionSort(self, A):
        """
        This function is used to sort list using insertion sort algorithm

        """

        for i in range(len(A)):
            temp = A[i]
            j = i - 1
            while j >= 0 and A[j] > temp:
                A[j + 1] = A[j]
                j = j - 1
            A[j + 1] = temp

        return A

    def MergeSort(self, A):
        """
        This function is used to sort list using merge sort algorithm
        """
        if len(A) < 2:
            return A

        mid = int(len(A) / 2)

        A1 = A[:mid]
        A2 = A[mid:]

        A1 = self.MergeSort(A1)
        A2 = self.MergeSort(A2)

        A = (
            A1 + A2
        )  # merge the two subarrays to create the new array with sorted halves

        i = 0
        j = 0
        aux = []
        while i <= len(A1) - 1 and j <= len(A2) - 1:
            if A1[i] <= A2[j]:
                aux.append(A[i])
                i += 1
            else:
                aux.append(A2[j])
                j += 1

        while i <= len(A1) - 1:
            aux.append(A1[i])
            i += 1

        while j <= len(A2) - 1:
            aux.append(A2[j])
            j += 1

        return aux

    def quicksort(self, A):
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
        A1 = self.quicksort(A[:p1])
        A2 = self.quicksort(A[p1 + 1 :])
        A = A1 + [A[p1]] + A2

        return A
