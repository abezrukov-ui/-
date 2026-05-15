def simmetr(s: str, i: int, j: int) -> bool:

    if i >= j:                 # базовый случай: дошли до середины
        return True
    if s[i] != s[j]:           # если символы не совпадают
        return False
    return simmetr(s, i + 1, j - 1)  # рекурсивная проверка
print(simmetr('hjjjjuiiiiu', 5, 10))