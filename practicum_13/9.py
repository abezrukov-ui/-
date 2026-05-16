import itertools

def task9(nums: str, k: int):
    numbers = list(map(int, nums.split()))
    return list(itertools.combinations(numbers, k))

print(task9("1 2 3 4", 2))
