def task3(sweet: str, friends: list[str]) -> int:
    sweet_set = set(sweet.split())
    friends_set = set().union(*[set(f.split()) for f in friends])
    return len(sweet_set - friends_set)
