'''Given the A and R i,e first term and common ratio of a GP series. Find the Nth term of the series.
Input: A = 2, R = 2, N = 4
Output: 16
Explanation: The GP series is 
2, 4, 8, 16, 32,... in which 16 
is th 4th term.'''


class Solution:
	def Nth_term(self, a, r, n):
		return a*(pow(r,n-1))

'''Driver code is at:
https://practice.geeksforgeeks.org/problems/series-gp4646/1#'''