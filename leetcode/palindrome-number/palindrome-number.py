#!/bin/python3

# Palindrome Number Algorithm
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Return False because there is no Palindrome of a Negative Number
        if x < 0:
            return False
        #Reverse String
        temp = x
        r = 0
        while(temp != 0):
            r = r * 10
            r = r + int(temp % 10)
            temp = int(temp/10)

        #Compare the reversed number with the real number
        if r == x:
            return True

        #If they are not Palindrome Number, return False
        return False
