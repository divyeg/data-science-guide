"""
Q1: Given an array of distinct integers candidates and a target integer target, return a list of all 
unique combinations of candidates where the chosen numbers sum to target. You may return the combinations 
in any order. The same number may be chosen from candidates an unlimited number of times. Two combinations 
are unique if the frequency of at least one of the chosen numbers is different.
"""


class Solution:
    """
    We use state space Tree method to solve this problem. There are other methods as well like using deque.
    We look for tree path until the current SUM is less than than target sum. If it is equal to targetSum,
    then we append the path to the result, if it is greater than targetSum then we return nothing
    """

    def combinationSum(self, candidates, target):
        self.res = set()
        self.candidates = candidates
        self.targetSum = target
        for i, num in enumerate(self.candidates):
            self.backtrack([num], i, num)
        return self.res

    def backtrack(self, path, i, currentSum):
        if currentSum >= self.targetSum:
            if currentSum == self.targetSum:
                pathTup = tuple(path)
                if pathTup not in self.res:
                    self.res.add(pathTup)
            return

        for j in range(i, len(self.candidates)):
            num = self.candidates[j]
            path.append(num)
            self.backtrack(path, j, currentSum + num)
            path.pop()


"""
Q2: There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0. You are given an integer array gain of length 
n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the 
highest altitude of a point.
"""


class Solution:
    def largestAltitude(self, gain):
        # start_time = time.time()
        alt = 0
        result = 0
        for i, j in enumerate(gain):
            alt = alt + j
            if alt > result:
                result = alt
        # print("Time taken: ", time.time() - start_time)
        return result


"""
Q3: Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target. You may assume that each input would have exactly one solution, and you may not use 
the same element twice. You can return the answer in any order.
"""


# Solution 1
class Solution:
    def twoSum(self, nums, target):
        result = {x: [i] for i, x in enumerate(nums)}
        for i, num in enumerate(nums):
            try:
                result[target - num].append(i)
                if len(set(result[num])) == 2:
                    return sorted(result[num])
            except:
                continue


# Solution 2 (faster)
class Solution:
    def twoSum(self, List, target):
        h = {}
        for i, num in enumerate(List):
            print(i, num)
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return (h[n], i)
