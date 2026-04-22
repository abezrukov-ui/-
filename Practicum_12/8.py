def fib(k: int) -> int:
    if k <= 0:
        return 0
    if k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)

print(fib(10))
