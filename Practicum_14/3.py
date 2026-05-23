def translate():
    n = int(input())
    dictionary = {}

    for _ in range(n):
        ru, en = input().split()
        dictionary[ru] = en
        dictionary[en] = ru

    word= input()
    if word in dictionary:
        print(dictionary[word])
    else:
        print(word)

translate()