def count(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a >= b:
        return a // b + count(a % b, b)
    else:
        return b // a + count(a, b % a)

print(count(10, 3))
