numbers = input()
print(sum(map(lambda x: 0 if int(x) % 2 == 1 else 1, numbers)))
