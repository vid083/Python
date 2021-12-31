# A generator to produce an infinite stream of fibonacci numbers. 
# The fibonacci series is a series where the next element is the sum of the last two elements.

def generate_fibonacci():
    n1 = 0
    yield n1
    
    n2 = 1
    yield n2
    
    while True:
        n1, n2 = n2, n1 + n2
        yield n2
        
seq = generate_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))

