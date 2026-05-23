def translate():
    n = int(input())
    dictionary = {}

    for _ in range(n):
        ru, en = input().split()
        dictionary[ru] = en

    phrase = input().split()

    result = []
    for word in phrase:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append(word)

    print(" ".join(result))
translate()