'''
Generators are a special type of iterator that generates values lazily.

They are defined useing the 'yield' keyword instead of 'return'.

Generators are memory efficient because they only generate values on the fly rather than storing them in memory.
'''

# fibonacci series
'''
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b
fib = fibonacci(5)
for num in fib:
    print(num)   '''
    
# sum of series
def series():
    sumresult = 0
    counter = 1
    while(counter <= 5):
        sumresult += counter*counter
        counter += 1
        yield (sumresult)
result = series()
for num in result:
    print(num)        