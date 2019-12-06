#!/bin/python3

# Given an array of integers
# return indices of the two numbers such that they add up to a specific target.
class Solution:

    def twoSum(self, nums, target):
        """
        Two Sum Algorithm
        Returns a list of indices which the sum belongs to the target

        Args:
            nums (list): list of integers
            target (int): Sum of the two elements

        Returns:
            List of intergers which the indexes belongs to the sum
        """
        t = {}
        for i, num in enumerate(nums):
            print(f"t : {t}")
            print(f"i : {i}")
            print(f"num : {num}")
            n = target - num
            print(f"target : {target}")
            print(f"n : {n}")
            if n not in t:
                #print(f" before t[num] : {t[num]}")
                t[num] = i
                print(f" after t[num] : {t[num]}")
                print(f"i : {i}")
            else:
                print(f"t[n] : {t[n]}")
                print(f"i : {i}")
                return [t[n], i]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 18
    solution = Solution()
    print(solution.twoSum(nums, target))
