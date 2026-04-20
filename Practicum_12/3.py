
def progress(a1: float,r: float,n:int) -> float:

    if n == 1:
        return n
    return a1 + progress(a1,r,n-1)
print(progress(1,1,3))