''''
0,0,2,1,4,2,6,3,8,4,
10,5,12,6,14,7,16,8
This series is a mixture of 2 series all the odd terms in this series form even numbers in ascending order
Every even terms is derived from the previous  term using the formula (x/2)
Write a program to find the nth term in this series.

The value n in a positive integer that should be read from STDIN the nth term that is calculated by the program should be written to STDOUT.
Other than the value of the nth term no other characters /strings or message should be written to STDOUT.
For example

if n=10,the 10 th term in the series is to be derived from the 9th term in the series. The 9th term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.
positions: 0,1,2,3,4,5,6,7,8,9
           0,0,2,1,4,2,6,3,8,4,
even positions - 0,2,4,6,8
odd positions - 0,1,2,3,4

steps:
1. for loop range(0,n)
2. check odd or even positions
    even - 
'''

def series(position):
    for i in range(0,position):
        if i % 2 == 0:
            a = i
            print(f"this is even position {i}, value {a}")
        else:
            a = (i//2)
            print(f"this is odd value {i}, value {a}")



series(10)


