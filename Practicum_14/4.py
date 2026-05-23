def find_form():
    n = int(input())
    dictionary = {}
    for _ in range(n):
        parts = input().split()
        form = parts[0]
        items = parts[1:]
        for item in items:
            dictionary[item] = form
    word = input().strip()
    print(dictionary.get(word, word))
find_form()