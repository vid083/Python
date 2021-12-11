''' Input : 122
Output: 221
Explanation: By reversing the digits of 
number, number will change into 221.
'''

class Solution:
	def reverse_digit(self, n):
	    res=0
        while n>0:
            digit=n%10
            res=res*10+digit
            n=n//10
        return res

''' Drive code is at https://practice.geeksforgeeks.org/problems/reverse-digit0316/1#'''