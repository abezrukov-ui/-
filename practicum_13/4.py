def task4(a: str, b: str, num: int) -> bool:
    set_a = set(map(int, a.split()))
    set_b = set(map(int, b.split()))
    intersection = set_a & set_b
    return num in intersection



print(task4("1 2 3", "2 3 4", 5))
