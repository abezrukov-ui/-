def ten_to_n(x: int, n: int) -> str:
    digits = "0123456789ABCDEF"       # цифры для систем до 16
    if x == 0:
        return "0"
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]

print(ten_to_n(255, 16))
