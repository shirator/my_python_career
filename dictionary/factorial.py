def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def factorials(n: int):
    factorial_dictionary = {}
    for i in range(1, n + 1):
        factorial_dictionary[i] = factorial(i)
    return factorial_dictionary
