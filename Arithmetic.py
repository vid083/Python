'''Given the first 2 terms A1 and A2 of an Arithmetic Series.Find the Nth term of the series. 
Input:
A1=2
A2=3
N=4
Output:
5
Explanation:
The series is 2,3,4,5,6....
Thus,4th term is 5. '''

class Solution:
    def nthTermOfAP(self,A1,A2,N):
        return A1+(N-1)*(A2-A1)

''' Drive code is at: 
https://practice.geeksforgeeks.org/problems/series-ap5310/1'''