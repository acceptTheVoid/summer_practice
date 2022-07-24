from sys import stdin

freq = {}

for line in stdin:
    stop = False
    words = line.split()
    for w in words: 
        if w == 'stop':
            stop = True
            break
        try:
            freq[w] += 1
        except KeyError:
            freq[w] = 1
    if stop: break

freq = sorted([(v, k) for k, v in freq.items()], key=lambda t: (-t[0], t[1]))
print(*[t[1] for t in freq], sep='\n', end='')
