def cache(func):
    memo = {}

    def wrapper(n):
        if n not in memo:
            memo[n] = func(n)
        return memo[n]

    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)