def degree5(n: int, k : int = 0 ) -> int:
    if n == 1:
        return k
    if n % 5 != 0:
        return -1
    return degree5(n // 5, k + 1)

print(degree5(125))
