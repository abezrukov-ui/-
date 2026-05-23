def task1(text: str):
    d = {}
    for word in text.split():
        d[word] = d.get(word, 0) + 1
    sg = sorted(d.items(), key=lambda x: -x[1])
    for i,o in sg:
        print(i)
task1("фп фh jпа фп")