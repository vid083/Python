''''
Case 1
Input: 4567
Expected Output: 2
Explanation : Odd positions are 4 and 6 as they are pos: 1 and pos: 3, both have sum 10. 
Similarly, 5 and 7 are at even positions pos: 2 and pos: 4 with sum 12. 
Thus, difference is 12 – 10 = 2

Case 2
Input: 5476
Expected Output: 2

code steps:
1. sum of odd, even positions
2. greater sum - less
3. 
'''

def diff(number):
    even = 0
    odd = 0
    count = 0
    for i in number:
        if count % 2 == 0:
            print(f"this is even position {i}, counter: {count}") 
            even += int(i)
        else:
            print(f"this is odd position {i}, counter: {count}")
            odd += int(i)
        count +=1
    print(even, odd)
    


diff("4567")