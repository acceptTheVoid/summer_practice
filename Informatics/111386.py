def generate(d):
    return [0, 0] if d == 1 else [generate(d - 1), generate(d - 1)]
    

dim = int(input())
print(generate(dim))
