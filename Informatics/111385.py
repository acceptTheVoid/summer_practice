diffs = []
for i in range(-1, 2):
    for j in range(-1, 2):
        if i != 0 or j != 0:
            diffs.append((i, j))

[n, m, k] = [int(i) for i in input().split()]

mines = [[int(i) for i in input().split()] for _ in range(k)]
field = [[0 for _ in range(m)] for _ in range(n)]
for [x, y] in mines:
    field[x - 1][y - 1] = '*'

for i in range(n):
    for j in range(m):
        if field[i][j] == '*':
            for x, y in diffs:
                x, y = i + x, j + y
                try:
                    if field[x][y] != '*' and x != -1 and y != -1:
                        field[x][y] += 1
                except IndexError:
                    pass

for i in range(n):
    for j in range(m):
        print(field[i][j], end=' ')
    print() 
