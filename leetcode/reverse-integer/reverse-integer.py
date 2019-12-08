#!/bin/python3

# Reverse Integer Algorithm
# Returns Reverted Integer
class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse Integer Algorithm
        Given a 32-bit signed integer, reverse digits of an integer.

        Args:
            x(int): Integer to be Reverted

        Returns:
            Reverted Integer
        """
        r = 0
        temp = abs(x)
        sign = 1
        if x <= 0:
            sign = -1
        while(temp != 0):
            r = r * 10
            r = r + int(temp%10)
            temp = int(temp/10)
        r = r * sign

        if r >= 2**31 -1 or r < -2**31:
            return 0

        return r
