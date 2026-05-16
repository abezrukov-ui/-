def task2(students: list[str]) -> int:
    sets = [set(s.split()) for s in students]
    # пересечение всех множеств
    common = set.intersection(*sets)
    return len(common)


print(task2(["math physics chemistry", "physics math", "math physics biology"]))
