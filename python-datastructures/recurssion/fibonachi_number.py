class fibonachi:
    def fibonachi_number(self, n):
        """
        Return the sum of two numbers
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            number = self.fibonachi_number(n - 1) + self.fibonachi_number(n - 2)
            return number


# if __name__ == "__main__":
#     f_seq = []
#     for i in range(5):
#         f_seq.append(fibonachi().fibonachi_number(i))
#     print(f_seq)
