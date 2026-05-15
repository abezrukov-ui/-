def search(a: list[int], x: int) -> int:
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)
print(search([1, 2, 3], 9))