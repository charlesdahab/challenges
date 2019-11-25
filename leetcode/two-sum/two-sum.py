#!/bin/python3

# Given an array of integers
# return indices of the two numbers such that they add up to a specific target.
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
            n = target - num
            if n not in h:
                t[num] = i
            else:
                return [t[n], i]
