import jieba
txt = open("沉默的羔羊.txt", "r", encoding="utf-8")
words = jieba.lcut(txt.read())
counts = {}
for word in words:
    if len(word) >= 2:
         counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse = True)
word, counts = items[1]
print(word)