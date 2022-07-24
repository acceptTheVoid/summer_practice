n = int(input())
latin = {}

for _ in range(n):
    english, translations = input().split(' - ')
    translations = translations.split(', ')
    for t in translations:
        try:
            latin[t].append(english)
        except KeyError:
            latin[t] = [english]

latin = sorted(list(latin.items()))
print(len(latin))
for i in latin:
    print(i[0], '- ', end='')
    print(*i[1], sep=', ') 
