# Create a generator function to generate an infinite stream of odd numbers and print the first 10 elements.

def generate_odd():
    n = 1
    while True:
        yield n
        n += 2

odd_generator = generate_odd()

for num in range(10):
    print(next(odd_generator))