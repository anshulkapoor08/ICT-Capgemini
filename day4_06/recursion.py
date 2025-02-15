'''
def factorial(n):
    if n == 0: # base case if n is 0, return 1
        return 1
    # recursive case: n*factorial(n-1)
    else:
        return n * factorial(n-1)
print (factorial(5)) '''   

# sum of series using recursion S = 1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2
def series(n):
    if n == 1:
        return 1
    else:
        return n*n + series(n-1)
print(series(6))   