import itertools

def task8(seq: str):
    nums = list(map(int, seq.split()))
    subsets = []
    for i in range(len(nums) + 1):
        subsets.extend(itertools.combinations(nums, i))
    return subsets


print(task8("1 2 3"))
