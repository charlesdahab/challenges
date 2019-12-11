#!/bin/python3

# Palindrome Number Algorithm
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        r = 0
        while(temp != 0):
            r = r * 10
            r = r + int(temp % 10)
            temp = int(temp/10)

        if r == x:
            return True

        return False
        
