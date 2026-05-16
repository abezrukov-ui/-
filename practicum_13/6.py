def task6():
    results = []
    for xod in range(100, 1000):
        mat = 3 * xod
        s_xod, s_mat = str(xod), str(mat)
        if len(s_mat) == 3 and len(set(s_xod + s_mat)) == len(s_xod + s_mat):
            results.append(f"{xod}+{xod}+{xod}={mat}")
    return results



print(task6()[:])
