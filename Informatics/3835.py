numbers = [int(n) for n in input().split()]
print(min(filter(lambda x: x > 0, numbers)))
