def odd_list(a: list[int], n: int) -> list[int]:

    if n == 0:
        return []
    rest = odd_list(a[1:], n - 1)
    return ([a[0]] if a[0] % 2 == 0 else []) + rest
