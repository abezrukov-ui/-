def gcd(a: int, b: int) -> int:
    if b == 0:          # базовый случай
        return a
    return gcd(b, a % b)  # рекурсивный вызов
print(gcd(2, 3))
