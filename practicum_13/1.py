def task1(seq: str, num: int) -> bool:
    nums = list(map(int, seq.split()))
    repeats = {x for x in nums if nums.count(x) > 1}
    return num in repeats
print(task1("1 2 1 3", 1))
