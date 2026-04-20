def mod_number(a: int,b: int) -> float:
    if a%b == a:
        return a
    return mod_number(a-b,b)
print(mod_number(16,5))