def sum_progress(a1: float,r: float,n:int) -> float:
    if n == 1:
        return a1
    return a1 +(n-1)*r + sum_progress(a1,r,n-1)
print(sum_progress(1,1,3))