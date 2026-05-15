def numbers(x: int) -> None:

    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)
print(numbers(10))