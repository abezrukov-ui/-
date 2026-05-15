def ind_maxlist(a: list[int], i: int = 0) -> int:

    if len(a) == 1:
        return i
    m_ind = ind_maxlist(a[1:], i + 1)
    return i if a[0] >= a[m_ind - i] else m_ind

print(ind_maxlist([1, 2, 3]))