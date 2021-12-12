''' You are given four numbers num1, den1, num2, and den2. You need to find (num1/den1)+(num2/den2) and output the result in the form of (numx/denx).

Input Format:
The first line of input contains an integer T denoting the number of test cases . Then T test cases follow . Each test case contains four integers num1, den1, num2, den2 respectively .

Output Format:
For each test case, in a new line,  output will be the fraction in the form a/b where the fraction denotes the sum of the two given fractions in reduced form.

Example:
Input
1
1 500 2 500
Output
3/500

Explanation:
In above test case 1/500+2/500=3/500
'''
import math
def addFraction(num1, den1, num2, den2):
    num=(num1*(den2)+num2*(den1))
    dem=(den1*den2)
    gcd=math.gcd(num,dem)
    print(str(num//gcd)+"/"+str(dem//gcd))

''' Driver code is at https://practice.geeksforgeeks.org/problems/add-two-fractions/1# 
'''