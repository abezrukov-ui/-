def ten_to_bin(x: int) -> str:
    if x == 0:
        return "0"
    if x == 1:
        return "1"
    return ten_to_bin(x // 2) + str(x % 2)

print(ten_to_bin(10))
