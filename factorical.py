def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  

def fibonacci(n):
    fib_series = []
    if n <= 0:
        return fib_series
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series


n_terms = 10
print("Fibonacci series up to {} terms:".format(n_terms))
print(fibonacci(n_terms))

 