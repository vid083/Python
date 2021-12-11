''' Given two numbers A and B, find Kth digit from right of A power B.
Example 1:
Input:
A = 3
B = 3
K = 1
Output:
7
Explanation:
33 = 27 and 1st
digit from right is 
7
'''
class Solution:
    def kthDigit(self, A, B, K):
        digit=A**B
        return str(digit)[-K]

''' Driver code is at https://practice.geeksforgeeks.org/problems/print-the-kth-digit3520/1# '''