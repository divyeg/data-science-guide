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
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return (h[n], i)


"""
Q4: An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game 
uses Dense Ranking, so its leaderboard works like this:
1. The player with the highest score is ranked number one on the leaderboard.
2. Players who have equal scores receive the same ranking number, and the next player(s) receive the 
immediately following ranking number.
Write a function that takes sequential player scores and return their leaderboard ranking based on the 
updated ranked list. Ranked list is sorted in descending order and players are sorted in ascending order
of their scores. Assume players completed the game in their order of scores.
"""


def climbingLeaderboard(ranked, player):
    # we remove duplicate scores from ranked players as it will not affect the rank of new players
    rankings = sorted(set(ranked), reverse=True)
    player_rank = []
    rank_index = 0
    player_index = -1
    minimum = -len(player)
    try:
        while player_index >= minimum:
            if player[player_index] >= rankings[rank_index]:
                player_rank.append(rank_index + 1)
                player_index -= 1
            else:
                rank_index += 1
    except IndexError:
        for i in range(minimum, player_index + 1):
            player_rank.append(rank_index + 1)
    return player_rank[::-1]


"""
Q5: Lexicographical order is often known as alphabetical order when dealing with strings. A string is 
greater than another string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This new word must meet two 
criteria:
1. It must be greater than the original word
2. It must be the smallest word that meets the first condition
"""


def biggerIsGreater(w):
    # find the latest element that has larger element after
    n = len(w)
    mx_sf_idx = n - 1
    swap_pos_l = None

    for i in range(n - 1, -1, -1):
        if w[i] < w[mx_sf_idx]:
            swap_pos_l = i
            break
        elif w[i] > w[mx_sf_idx]:
            mx_sf_idx = i

    # sequence is the largest permutation
    if swap_pos_l is None:
        return "no answer"

    # find smallest larger element
    swap_pos_r = swap_pos_l + 1
    for i in range(swap_pos_l + 1, n):
        if w[i] < w[swap_pos_r] and w[i] > w[swap_pos_l]:
            swap_pos_r = i

    # swap
    w_arr = list(w)
    l_tmp = w_arr[swap_pos_l]
    w_arr[swap_pos_l] = w_arr[swap_pos_r]
    w_arr[swap_pos_r] = l_tmp

    # sort and build the solution
    w_arr_l = w_arr[: swap_pos_l + 1]
    w_arr_r = w_arr[swap_pos_l + 1 :]
    w_arr_r.sort()

    return "".join(w_arr_l + w_arr_r)


"""
Q6: Given a list of non-negative integers nums, arrange them such that they form the largest number 
and return it. For example nums = [10,2], output = "210"

"""


def LargestNumber(nums):
    return (
        "".join(sorted([str(num) for num in nums], key=lambda x: x * 10, reverse=True))
        if set(nums) != set([0])
        else "0"
    )


"""
Q7: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the 
two sorted arrays.

"""


def findMedianSortedArrays(nums1, nums2):
    merged_nums = []
    i = j = 0
    total_length = len(nums1) + len(nums2)

    while i + j < total_length and i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_nums.append(nums1[i])
            i += 1
        else:
            merged_nums.append(nums2[j])
            j += 1
    if j <= len(nums2):
        merged_nums.extend(nums2[j:])

    if i <= len(nums1):
        merged_nums.extend(nums1[i:])

    if total_length % 2 == 0:
        median_num = (
            merged_nums[total_length // 2] + merged_nums[(total_length // 2) - 1]
        ) / 2
    else:
        median_num = merged_nums[total_length // 2]
    return median_num


"""
Q8:There are two lists of dictionaries representing friendship beginnings and endings: friends_added 
and friends_removed. Each dictionary contains the user_ids and created_at time of the friendship 
beginning /ending.

Write a function friendship_timeline to generate an output that lists the pairs of friends with 
their corresponding timestamps of the friendship beginning and then the timestamp of the friendship 
ending.

Note: There can be multiple instances over time when two people became friends and unfriended; 
only output lists when a corresponding friendship was removed.

Example:

Input:

friends_added = [
    {'user_ids': [1, 2], 'created_at': '2020-01-01'},
    {'user_ids': [3, 2], 'created_at': '2020-01-02'},
    {'user_ids': [2, 1], 'created_at': '2020-02-02'},
    {'user_ids': [4, 1], 'created_at': '2020-02-02'}]

friends_removed = [
    {'user_ids': [2, 1], 'created_at': '2020-01-03'},
    {'user_ids': [2, 3], 'created_at': '2020-01-05'},
    {'user_ids': [1, 2], 'created_at': '2020-02-05'}]

Output:

friendships = [{
    'user_ids': [1, 2],
    'start_date': '2020-01-01',
    'end_date': '2020-01-03'
  },
  {
    'user_ids': [1, 2],
    'start_date': '2020-02-02',
    'end_date': '2020-02-05'
  },
  {
    'user_ids': [2, 3],
    'start_date': '2020-01-02',
    'end_date': '2020-01-05'
  },
]
"""
