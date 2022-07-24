n = int(input())
variants = {'read': 'R', 'write': 'W', 'execute': 'X'}
files = {}
for _ in range(n):
    file, *premissions = input().split()
    files[file] = frozenset(premissions)


ops = int(input())
for _ in range(ops):
    op, file = input().split()
    if variants[op] in files[file]: print('OK')
    else: print('Access denied')
