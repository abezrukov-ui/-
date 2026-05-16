import itertools

def task7(seq: str):
    nums = list(map(int, seq.split()))
    return list(itertools.permutations(sorted(nums)))


print(task7("1 2 3"))
