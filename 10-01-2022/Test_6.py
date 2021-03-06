''''
Question. Find the nth term of the series.

1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243,64, 729, 128, 2187 ….

This series is a mixture of 2 series – all the odd terms in this series form a geometric series and all the even terms form yet another geometric series. Write a program to find the Nth term in the series.

The value N in a positive integer that should be read from STDIN.
The Nth term that is calculated by the program should be written to STDOUT.
Other than value of n th term,no other character / string or message should be written to STDOUT.
For example , if N=16, the 16th term in the series is 2187, so only value 2187 should be printed to STDOUT.
You can assume that N will not exceed 30.

Link to this Question : https://prepinsta.com/tcs-write-a-program-find-the-nth-term-of-the-series-112349827168132243/

Test Case 1

Input- 16
Expected Output – 2187
Test Case 2

Input- 13
Expected Output – 64

positions:  1, 2, 3, 4, 5, 6, 7,  8,  9, 10
            1, 1, 2, 3, 4, 9, 8, 27, 16, 81

odd positions- 1,2,4,8,16
even - 1,3,9,27
'''

def gp(position):
    
    if position % 2 != 0:
        term = position//2
        print(term)
        res = pow(2,term)
        print(f"this is odd, {position} position, GP of 2, result is {res}")
    else:
        term = (position//2) - 1
        print(term)
        res = pow(3,term)
        print(f"this is even, {position} position, GP of 3, result is {res}")

# gp(5)
gp(6)
# gp(7)
gp(8)
gp(16)
gp(13)
        
