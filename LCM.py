''' Given two numbers A and B. The task is to find out their LCM and GCD.
Example 1:

Input:
A = 5 , B = 10
Output:
10 5
Explanation:
LCM of 5 and 10 is 10, while
thier GCD is 5.
'''
import math
class Solution:
    def lcmAndGcd(self, A , B):
        lcm=(A*B)//math.gcd(A,B)
        gcd=math.gcd(A,B)
        return lcm,gcd

''' Driver code is at https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1#
'''